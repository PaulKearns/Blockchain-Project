import sys
import socket
import pickle
import signal

def exit_sequence(sig, frame):
    '''
    - logging that the tracker is exiting
    - exiting the tracker
    '''
    print('exiting')
    sys.exit()

def tracker(port):
    '''
    - receiving incoming connections from nodes
    - adding the nodes to the list of nodes
    - sending the list of nodes to the nodes
    '''
    nodes = set()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port)) 
    s.listen()
    print(f'listening on port {port}')
    while True:
        c, _ = s.accept()
        data_length = int.from_bytes(c.recv(4), 'big')
        if not data_length:
            binary = pickle.dumps(nodes)
            c.sendall(len(binary).to_bytes(4, 'big') + binary)
            continue
        node_info = pickle.loads(c.recv(data_length))
        if node_info[0] == 'A':
            nodes.add(node_info)
        elif node_info[0] == 'R':
            print(f'removing {node_info[1]}:{node_info[2]}')
            nodes.discard(('A', node_info[1], node_info[2]))
            nodes.add(node_info)
        binary = pickle.dumps(nodes)
        # assume that the size of the binary is less than 2^32
        c.sendall(len(binary).to_bytes(4, 'big') + binary)
        c.close()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_sequence)
    tracker(int(sys.argv[1]))