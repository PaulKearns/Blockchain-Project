import random
import sys
import socket
import pickle
import threading
import time
import block_chain
import signal
import os

socks = {} # K = (node_ip, node_port), V = Socket TCP connection to node
bc = block_chain.BlockChain()
tracker_sock = 0
sock_lock = threading.Lock()
chain_lock = threading.Lock()
node_port = random.randint(49152, 65535)

# Node communication codes:
# A: application, B: block, C: chain, D: don't not give me your chain

# On each vm
# sudo apt install python3-pip
# pip install psutil

def exit_sequence(_, __):
    '''
    - sending a message to the tracker that this node is exiting
    - ending the node process
    '''
    print('exiting')
    tracker_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    node_info = ('R', sys.argv[3], node_port)
    binary = pickle.dumps(node_info)
    try:
        tracker_sock.connect((sys.argv[1], int(sys.argv[2])))
        tracker_sock.sendall(len(binary).to_bytes(4, 'big') + binary)
    except:
        pass

    # close all sockets
    for s in socks:
        socks[s].close()
    tracker_sock.close()
    os._exit(0)


def print_chain():
    '''
    - storing the chain in a string
    - printing the chain to the console
    '''
    n = bc.header.next
    i = 1
    str = ''
    while n is not bc.trailer:

        str += f'block {i}: {n.block.data}\n'
        i += 1
        n = n.next
    if str:
        print(str.strip())

    

def contact_tracker(tracker_ip, tracker_port, node_ip):
    '''
    - sending this node's information to the tracker
    - receiving all node information from the tracker
    - connecting to the active nodes
    '''
    node_info = ('A', node_ip, node_port)
    binary = pickle.dumps(node_info)
    while True:
        tracker_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tracker_sock.connect((tracker_ip, tracker_port))
            tracker_sock.sendall(len(binary).to_bytes(4, 'big') + binary)
            topology_length = int.from_bytes(tracker_sock.recv(4), 'big')
            topology = pickle.loads(tracker_sock.recv(topology_length))
        except:
            print("connection to tracker failed")
            sys.exit()
        topology = list(topology)
        # Make sure removed records come first to handle node rejoins
        topology.sort(key = lambda x: x[0], reverse = True)
        sock_lock.acquire()
        for node in topology:
            s = (node[1], node[2])
            if s[0] == node_ip:
                continue
            if s not in socks and node[0] == 'A': # A means active here
                socks[s] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    socks[s].connect(s)
                    print(f"established connection with {s}")
                except Exception as e:
                    print(f"error trying to establish connection with {s}:{e}")
                    socks[s].close()
                    del socks[s]
            elif s in socks and node[0] == 'R':
                print(f"removed connection with {s}")
                del socks[s]
        sock_lock.release()
        time.sleep(1)
        tracker_sock.close()



def accept_connections():
    '''
    - accepting incoming connections
    - redirect connection to data receiving thread
    '''
    node_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    node_sock.bind(('0.0.0.0', node_port))
    node_sock.listen()
    print(f'listening on port {node_port}')
    while True:
        c, addr = node_sock.accept()
        print(f'established connection with {addr[0]}')
        t = threading.Thread(target=receive_msg, args=(c,))
        t.start()

def receive_msg(c):
    '''
    - receiving incoming connections
    - calling the appropriate function based on the received code
    '''
    while True:
        try:
            code = c.recv(1).decode()
            print(f'received from {c.getpeername()}: {code}')
        except Exception as e:
            print(f'disconnecting from {c.getpeername()}')
            c.close()
            return
        if code == 'A':
            add_block(c)
        elif code == 'B':
            update_chain(c)
        elif code == 'C':
            receive_chain(c)
        elif code == 'D':
            print('got chain request')
            send_chain(c)
        elif code == '':
            c.close()
            print(f"received empty payload, disconnecting" +
                  f"from {c.getpeername()}")
            return

def add_block(c):
    '''
    - receiving data from the application
    - mining a new block to store the data
    - sending the new block to all connected nodes
    '''
    try:
        data_length = int.from_bytes(c.recv(4), 'big')
        data = pickle.loads(c.recv(data_length))
    except Exception:
        print(Exception)
        return
    chain_lock.acquire()
    rc = bc.mine(data)
    chain_lock.release()
    if rc:
        print(f'failed to mine block for data: {data}')
        return
    sock_lock.acquire()
    for node in socks:
        binary = pickle.dumps(bc.trailer.prev.block)
        try:
            socks[node].sendall(b'B' + len(binary).to_bytes(4, 'big') + binary)
            print(f"sent to {node}")
        except:
            del socks[node]
    sock_lock.release()

    print_chain()

def update_chain(c):
    '''
    - receiving a block from another node
    - validating the block
    - adding the block to the chain if it is valid
    - requesting the chain from the node if it might be longer
    '''
    try:
        data_length = int.from_bytes(c.recv(4), 'big')
        block = pickle.loads(c.recv(data_length))
    except:
        return
    chain_lock.acquire()
    if bc.validate(block):
        bc.add(block)
    elif block.block_id > bc.length and block.this_hash[:3] == '000':
        try:
            sent = False
            for node_info in socks.keys():
                if node_info[0] == c.getpeername()[0]:
                    socks[node_info].sendall(b'D')
                    print(f'sent chain request to {node_info}')
                    sent = True
                    break
            if not sent:
                print(f'Failed to send chain request to {c.getpeername()[0]}')
        except:
            chain_lock.release()
            return
    chain_lock.release()

    print_chain()

def receive_chain(c):
    '''
    - receiving a potentially longer chain from another node
    - validating the chain which confirms it is longer
    - replacing the current chain with the new chain if it is valid
    '''
    try:
        data_length = int.from_bytes(c.recv(4), 'big')
        chain = pickle.loads(c.recv(data_length))
    except:
        return
    new_chain = block_chain.BlockChain()
    while chain.header.next is not chain.trailer:
        block = chain.header.next.block
        chain.header.next = chain.header.next.next
        if not new_chain.validate(block):
            print(f'got a bad chain from {c.getpeername()}')
            return
        new_chain.add(block)
    chain_lock.acquire()
    global bc
    bc = new_chain
    chain_lock.release()

    print_chain()

def send_chain(c):
    '''
    - putting the chain into a binary format
    - sending the chain to the requesting node
    '''
    chain_lock.acquire()
    binary = pickle.dumps(bc)
    chain_lock.release()
    try:
        sent = False
        for node_info in socks.keys():
            if node_info[0] == c.getpeername()[0]:
                socks[node_info].sendall(b'C' + len(binary).to_bytes(4, 'big')
                                         + binary)
                print(f'sent chain to {node_info} upon request')
                sent = True
                break
        # means request came from display program
        if not sent:
            c.sendall(len(binary).to_bytes(4, 'big') + binary)
    except:
        pass   

# Usage: python3 node.py <tracker_ip> <tracker_port> <node_ip> <node_port>
if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_sequence)
    t1 = threading.Thread(target=contact_tracker, args=(
        sys.argv[1], int(sys.argv[2]), sys.argv[3]))
    t1.start()
    t2 = threading.Thread(target=accept_connections)
    t2.start()
    t1.join()

