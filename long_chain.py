import block_chain
import socket
import sys
import pickle
import random
import threading
import time
import signal

# Run on shop/tracker vm in isolated terminal
# Enter the shop's port as the first argument
# Don't enter a second argument to keep the chain clean
# Enter 'bad' as the second argument to corrupt the data in the first block

# Creates a blockchain with 10 blocks
# Sends the last block in its blockchain to a random node
# Receives a request for its blockchain if the node's chain is shorter
# Sends its blockchain to the node

socks = {}
bc = block_chain.BlockChain()
port = random.randint(49152, 65535)
# don't want collision with tracker
while port == sys.argv[1]:
    port = random.randint(49152, 65535)


def exit_sequence(_, __):
    '''
    - sending a message to the tracker that this node is exiting
    - ending the node process
    '''
    print('exiting')
    node_info = ('R', sys.argv[2], port)
    binary = pickle.dumps(node_info)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', int(sys.argv[1]))) # tracker port
    s.sendall(len(binary).to_bytes(4, 'big') + binary)

    # close all sockets
    for sck in socks:
        socks[sck].close()

    s.close()
    sys.exit()

def accept_connections(node_port):
    '''
    - accepting a connection
    - get the chain request
    '''
    node_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    node_sock.bind(('0.0.0.0', node_port))
    node_sock.listen()
    print(f'listening on {port}')
    while True:
        c, addr = node_sock.accept()
        print(f'established connection with {addr[0]}')
        t = threading.Thread(target=receive_msg, args=(c,), daemon=True)
        t.start()

def receive_msg(c):
    code = c.recv(1).decode()
    if code == 'D':
        print('got chain request')
        if len(sys.argv) > 3 and sys.argv[3] == 'bad':
            bc.header.next.block.data = 'bad data'
        binary = pickle.dumps(bc)
    else:
        return
    try:
        sent = False
        for node_info in socks.keys():
            if node_info[0] == c.getpeername()[0]:
                socks[node_info].sendall(b'C' + len(binary).to_bytes(4, 'big')
                                         + binary)
                print(f'sent chain to {node_info} upon request')
                sent = True
                break
        if not sent:
            print(f'Failed to send chain to {c.getpeername()[0]} upon request')
    except:
        pass


for i in range(20):
    bc.mine(f'Monkey {i}')


# start server thread
t = threading.Thread(target=accept_connections, args=(port,), daemon=True)
t.start()
time.sleep(1)

# get topology from tracker
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', int(sys.argv[1]))) # tracker port
node_info = ('A', sys.argv[2], port) # tracker ip
binary = pickle.dumps(node_info)
s.sendall(len(binary).to_bytes(4, 'big') + binary)
topology_length = int.from_bytes(s.recv(4), 'big')
topology = pickle.loads(s.recv(topology_length))
topology = list(topology)
topology.sort(key = lambda x: x[0], reverse = True)
for node in topology:
    s = (node[1], node[2])
    if s[0] == sys.argv[2]:
        continue
    if s not in socks and node[0] == 'A':
        socks[s] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socks[s].connect(s)
    elif s in socks and node[0] == 'R':
        del socks[s]

# send last block in chain to random node
node = random.choice(list(socks.keys()))
binary = pickle.dumps(bc.trailer.prev.block)
time.sleep(5)
socks[node].sendall(b'B' + len(binary).to_bytes(4, 'big') + binary)
print(f'sent block to random node: {node}')
signal.signal(signal.SIGINT, exit_sequence)
t.join()