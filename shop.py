import sys
import socket
import random
import pickle

socks = {}
record = {}
tracker_ip = 'localhost'
tracker_port = 0

def update_blockchian():
    '''
    - connecting to the tracker
    - receiving the topology from the tracker
    - connecting to the active nodes
    - sending the record to a random active node
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((tracker_ip, tracker_port))
        s.sendall(b'\x00\x00\x00\x00')
        topology_length = int.from_bytes(s.recv(4), 'big')
        topology = pickle.loads(s.recv(topology_length))
    except:
        print('Connection to tracker failed')
        sys.exit()
    topology = list(topology)
    topology.sort(key = lambda x: x[0], reverse = True)
    for node in topology:
        s = (node[1], node[2])
        if s not in socks and node[0] == 'A':
            socks[s] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                socks[s].connect(s)
            except:
                del socks[s]
        elif s in socks and node[0] == 'R':
            print(f"Removed connection with {s}")
            del socks[s]
    node = random.choice(list(socks.keys()))
    binary = pickle.dumps(record)
    try:
        print(f'Updating record in blockchain at {node}')
        # possible for this to succeed even if node is offline
        # when node closes socket, it does not send a FIN packet
        socks[node].sendall(b'A' + len(binary).to_bytes(4, 'big') + binary)
    except:
        del socks[node]
        print('Definately failed to update record in blockchain')
        print('Next record update will probably bring blockchain up to date')

if __name__ == '__main__':

    tracker_port = int(sys.argv[1])

    # shop inventory
    shop = [('baboon', '🦧30', 'https://en.wikipedia.org/wiki/Papio'),
        ('gorilla', '🦧200', 'https://en.wikipedia.org/wiki/Gorilla'),
        ('orangutan', '🦧100', 'https://en.wikipedia.org/wiki/Orangutan'),
        ('chimpanzee', '🦧50', 'https://en.wikipedia.org/wiki/Chimpanzee'),
        ('howler monkey', '🦧10',
         'https://en.wikipedia.org/wiki/Howler_monkey'),
        ('spider monkey', '🦧10',
         'https://en.wikipedia.org/wiki/Spider_monkey'),
        ('atlantic forest titi monkey', '🦧69',
         'https://en.wikipedia.org/wiki/Callicebus'),
        ('squirrel monkey', '🦧10',
         'https://en.wikipedia.org/wiki/Squirrel_monkey'),
        ('pygmy marmoset', '🦧10',
         'https://en.wikipedia.org/wiki/Pygmy_marmoset'),
        ('woolly monkey', '🦧420', 'https://en.wikipedia.org/wiki/Lagothrix')]
    
    # initial name prompt, record creation, and shop display
    name = input('What is your name? ')
    record[name] = [1000, []]
    update_blockchian()
    print(f'Welcome to the 🦧 shop, {name}!')
    print('Here is what we have for sale:')
    for i in range(len(shop)):
        print(f'{i + 1}. {shop[i][0]} {shop[i][1]} {shop[i][2]}')

    # shop loop
    while True:
        print(f'Balance: {record[name][0]}')
        print(f'Cart: {record[name][1]}')
        choice = input('Enter p for purchase or n for new shopper: ')
        if choice == 'n':
            name = input('What is your name? ')
            if name not in record:
                record[name] = [1000, []]
                update_blockchian()
            print(f'Welcome to the 🦧 shop, {name}!')
            print('Here is what we have for sale:')
            for i in range(len(shop)):
                print(f'{i + 1}. {shop[i][0]} {shop[i][1]}')
        elif choice == 'p':
            item = input('Which item # would you like to purchase? ')
            if item.isdigit() and 1 <= int(item) <= 10:
                item = int(item)
            else:
                print('Invalid input. Please try again.')
                continue
            if record[name][0] >= int(shop[item - 1][1][1:]):
                record[name][0] -= int(shop[item - 1][1][1:])
                record[name][1].append(shop[item - 1][0])
                update_blockchian()
                print(f'You have purchased a {shop[item - 1][0]}!')
            else:
                print('You do not have enough apecoins to make that purchase.')
        else:
            print('Invalid input. Please try again.')