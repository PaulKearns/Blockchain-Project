### High Level Ideas
The whole program depend on the following three parts: blockchain implementation, peer-to-peer network, and application layer program. The following is an overview of the whole program. Detailed implementation will be described later.  
  
1. We first start the tracker program. When a new node joins, it will contact the tracker to get information about the other nodes, so that it can be part of a peer-to-peer connection with all other nodes. When a node leaves the network, it will also contact the tracker about its leaving, so that all other nodes will close the connection to the node.  

2. Each node will periodically contact the tracker to learn the most up-to-date information about the network's topology, including which of the nodes are still alive and which of them have left.  

3. Each node will have functionality to mine blocks and broadcast them to all other nodes. Each node will also have functionality to receive blocks from all other nodes and verify them. If a received block is valid, the node will accept it and add it to its local blockchain. If the block has a higher ID number, it will request the whole chain from the node it got the block from. If the block is invalid, the node refuses the incoming block.  

4. Our blockchain will apply to a currency that can be used in an online shop. When a transaction occurs, the application layer will contact a node. The node will mine a new block to record the shop's most up-to-date record and broadcast to all other nodes.  

5. Everytime a new shopper joins they will have 1000 coins to spend. A new shopper joining will trigger a new block to be added to the chain. Each block will store information about every user.  

### BlockChain Implementation
This part describes the data structures and functions used to implement the blockchain technology. There are three classes:  
1. Block Class:  
Class for a block in the blockchain.  
Fields:  
&#8226;&#xfe0e; `block_id`: Unique identifier for the block.  
&#8226;&#xfe0e; `nonce`: Number incremented to find a valid hash.  
&#8226;&#xfe0e; `this_hash`: Hash of the block.  
&#8226;&#xfe0e; `prev_hash`: Hash of the previous block.  
&#8226;&#xfe0e; `data`: Data stored in the block.  
2. BlockChain Class:  
Class for block chain which contains a list of blocks.  
Fields:  
&#8226;&#xfe0e; `header`: First node in the chain. (Sentinel)  
&#8226;&#xfe0e; `trailer`: Last node in the chain. (Sentinel)  
&#8226;&#xfe0e; `length`: Number of blocks in the chain.  
Functions:  
&#8226;&#xfe0e; `mine(data)`: Mines a new block by calculating its hash, incrementing the nonce until a valid hash is found, and adding the block to the chain. Dynamic mining difficulty is implemented so that if a node is at higher CPU usage, it is harder to mine a block, using the psutil library.  
&#8226;&#xfe0e; `validate(block)`: Validates a block by checking if it's the first block in the chain, if the previous hash matches the hash of the previous block, if the hash of the block is correct, if it has three leading zeros, and if its block id is sequential.  
&#8226;&#xfe0e; add(block): Adds a new block to the end of the chain by creating a new node with the block and updating the pointers.  
3. Node Class:  
Class for a node to store its information.  
Fields:  
&#8226;&#xfe0e; `block`: Block stored in the node.  
&#8226;&#xfe0e; `next`: Reference to the next node in the chain.  
&#8226;&#xfe0e; `prev`: Reference to the previous node in the chain.  

### Peer-To-Peer Network  

Our implementation uses a peer-to-peer network with peers/nodes and one tracker/server. These are split into two files:  
1. node.py:  
Program that makes a vm be a peer in the network. Launches thread to contact the tracker once every second to update socket connections to peers, and uses another thread to accept new connections and open a new thread for each new connection. These threads will respond to and make requests.  
Command line arguments:  
&#8226;&#xfe0e; `tracker_ip`: The IP address of the machine the tracker is run on.  
&#8226;&#xfe0e; `tracker_port`: The port that the tracker is listening on.  
&#8226;&#xfe0e; `node_ip`: The IP address of the current machine.  
Global variables:  
&#8226;&#xfe0e; `socks`: Dictionary with key of tuple of (node_ip, node_port) of another node/peer, and value of socket connection with that node.  
&#8226;&#xfe0e; `bc`: The BlockChain object that represents the current chain recorded by this node.  
&#8226;&#xfe0e; `tracker_sock`: The socket by which to contact the tracker.  
&#8226;&#xfe0e; `sock_lock`: Lock for threads to access the sock dictionary.  
&#8226;&#xfe0e; `chain_lock`: Lock for threads to access the BlockChain object bc.  
&#8226;&#xfe0e; `node_port`: The current port that the node is listening on. This is selected as a random integer from 49152 to 65535, and is chosen randomly so that if the node was recently running, then exited and restarted, the node is unlikely to open a socket on the same port that is already occupied. If it does select the same number, the node will fail to restart and must be restarted again.  
Functions:  
&#8226;&#xfe0e; `exit_sequence(sig, frame)`: Sends a message to the tracker that the node is exiting, and closes all socket connections. Triggered by SIGINT kill signal, given by command line on the machine.  
&#8226;&#xfe0e; `print_chain()`: Converts the chain to a string format and prints to stdout.  
&#8226;&#xfe0e; `contact_tracker(tracker_ip, tracker_port, node_ip, node_port)`: Contacts the tracker with information about self and updates socks dictionary as necessary once every second. The program reverse sorts the topology received from the tracker by the code for a node's status: 'R' = Removed, 'A' = Active. This reverse sort ensures that removed nodes are dealt with first, so that if a node leaves and then rejoins, it will be marked as active ultimately.  
&#8226;&#xfe0e; `accept_connections(node_port)`: Constantly waits for and accepts new connections, then opens a new thread to interact with that connection.  
&#8226;&#xfe0e; `receive_msg(c)`: Listens over connection c for incoming one letter codes (A - application layer, B - new block, C - full blockchain, D - request to send self's chain to that node), and calls the appropriate function based on that code. If an empty string is received, close the connection because it is broken or ended.  
&#8226;&#xfe0e; `add_block(c)`: Receives and deserializes information for a new block from the application layer, mines a new block, and sends to all other connected nodes.  
&#8226;&#xfe0e; `update_chain(c)`: Receives a new block from another node. If the new block's ID is higher than the next block's ID should be, it sends a chain request. Otherwise, verify the block and add it to the blockchain. If the verification fails, do nothing. Sends the chain request by iterating through all sockets in socks until the IP of the given socket matches that of the connection that the block was received from, when the program sends a chain request and exits the loop.  
&#8226;&#xfe0e; `receive_chain(c)`: Receives and deserializes a chain from connection c, then validates the chain and checks if it is longer than the current chain. If it is longer, replace the current chain with the new chain. This is how forks are dealt with: the longest valid chain is correct.  
&#8226;&#xfe0e; `send_chain(c)`: Sends the chain to the node with the connection c. Since the other node only receives over its server socket, the program finds this server socket in the socks dictionary by iterating through each key in socks until the IP address matches that of the connection, indicating it is the correct node to send to.  
2. tracker.py  
File to run the tracker, which is essentially a server used for sending all active nodes to other nodes in the peer-to-peer network.  
Command line arguments:  
&#8226;&#xfe0e; `tracker_port`: The port that the tracker should listen on.  
Functions:  
&#8226;&#xfe0e; `exit_sequence(sig, frame)`: Sends a message to the tracker that the node is exiting, and closes all socket connections. Triggered by SIGINT kill signal, given by command line on the machine.  
&#8226;&#xfe0e; `tracker(port)`: Receives incoming connections from nodes over a server socket at (tracker_port, tracker_ip), removes the node if signaled by code 'R', and otherwise adds the node to the set of active nodes if not present, before sending the current set of all nodes to that node.  

### Application  

Our application is essentially a store/marketplace to buy different types of monkeys using the currency. This is run on file shop.py.  
1. shop.py  
The shop offers a user options to create/select a new user, or purchase a monkey from a list of monkeys printed to the terminal. Upon a change to the record, which occurs with every action by the user, the shop contacts the tracker and selects an active node at random to mine a new block with the updated record. There should only be one instance of this program run and it should always be for a freshly started blockchain network. With multiple shops running, the network will contain intermingled records from different shops. If the network is not restarted when the shop is, there will be blocks at the beginning of the chain from a dead shop.  
Command line arguments:  
&#8226;&#xfe0e; `tracker_port`: The port that the tracker is listening on.  
Global variables:  
&#8226;&#xfe0e; `socks`: Dictionary with key of tuple of (node_ip, node_port) of a node/peer, and value of socket connection with that node.  
&#8226;&#xfe0e; `record`: Dictionary with key of user (string), and value of list of monkeys (string) in cage.  
&#8226;&#xfe0e; `tracker_port`: The port by which to contact the tracker.  
&#8226;&#xfe0e; `tracker_ip`: The IP address used for contacting the tracker. This is currently hardcoded as localhost, because in this implementation we run the shop on the same VM as the tracker.  
Functions:  
&#8226;&#xfe0e; `update_blockchain()`: Sends a message to the tracker to retrieve the set of all nodes, and selects a random active node to send the current (updated) record to.  

### Graphics  

We have an animation to represent and help visualize the growing block chain. This is run locally on a Chrome browser via visual.py.  
1. visual.py  
Communicates through a socket connection with a node to request block chain updates. Launches and dynamically updates the website to display the current block chain.  
&#8226;&#xfe0e; `port`: The port number of the node whose block chain will be displayed.  
&#8226;&#xfe0e; `ip`: The id address of the node whose block chain will be displayed.  
&#8226;&#xfe0e; `driver`: The webdriver element used to load the and reload our locally hosted website.  
&#8226;&#xfe0e; `js_data`: Dictionary representation of the block chain, updated as the block chain grows.  
&#8226;&#xfe0e; `generate_js()`: Writes to and updates the visual.js file, to get the changes to the block chain.  
&#8226;&#xfe0e; `generate_html()`: Open the initial blank website on the chrome browser.  
&#8226;&#xfe0e; `reload_html`: Update the visual.js script and reload the website to reflect those changes.  
&#8226;&#xfe0e; `visual()`: Send a request to the node for the current block chain. Receive the block chain and parse its values. If there are no updates we can request again, otherwise we will change, and reload the website to reflect these changes.  
2. visual.html  
A basic html file to generate the outline of our website. Contains a reference to visual.js for dynamic updates to the visuals on the website.  
3. visuals.css  
Defines the styles for the visuals on the website. Creates the individual items and containers which hold the pictures and values that are displayed.  
4. visual.js  
Allows for dynamic changes to the website. Rather than hard coding the amount of blocks that show up in the html script, we can edit the dictionary referenced in visual.js. It loops through the dictionary and adds the amount of blocks to the page, as well as the chain link pictures.