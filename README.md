# Blockchain Cryptocurrency Project
## Paul Kearns
  
This project, the final project for my Computer Networks class, involved creating a simplified peer-to-peer blockchain along with a toy application in a group with three other students. Blockchain, a distributed mechanism invented in 2008 for Bitcoin, allows nodes in a network to agree on a state without mutual trust. It operates as a linked list of blocks, each containing a cryptographic hash of the previous block, ensuring data integrity. Blockchains resist data modification, making them suitable for various applications beyond cryptocurrencies. Typically, blockchains are managed by a peer-to-peer network where each node stores the entire blockchain, forming a distributed ledger.  
  
### Features:  
We implemented a simple peer-to-peer network with blockchain objects. In addition, we made a small application, shop.py, which utilizes block chain for record keeping. This is the complete list of features:  
  
1. peer-to-peer network with tracker and clients:  
	- tracker.py maintains a list of peers that updates when peers join or leave  
	- peers maintain a connection to the tracker and all other peers  
2. a basic blockchain implementation where each node:  
	- maintain a copy of the blockchain  
	- mine to create a valid block and add it to the blockchain after receiving data from shop.py  
	- broadcast mined blocks to other peers  
	- verify blocks received by other peers and add them to its own blockchain  
	- request a node's blockchain if it is suspected to be longer than its own  
    - send its blockchain to a node that requests it  
    - replace its blockchain with a longer one if it receives one (fork resolution)  
3. application, shop.py: 
	- users can create accounts, buy monkeys, and switch between accounts  
    - all actions are performed in the terminal  
    - the shop's record is updated locally after each transaction and account addition  
    - everytime the shop's local record is updated, the shop sends its record to a random node in the blockchain network. The node mines a block with the shop's most up-to-date record and broadcasts it to the network  
4. a graphical representation of blockchain:  
    - visual.py, visual.css, visual.js, and visual.html work together with node.py to display the contents of a node's blockchain in a browser  
    - the blockchain is displayed as a series of blocks with all of their components  
    - the blockchain is updated in real-time as new blocks are mined and added to the blockchain  
    - visual.py is run locally and continuously requests the blockchain from a node in the network  
5. dynamic adjustment of mining difficulty:  
    - the mining difficulty at a node is based on how strained the device running node.py is; the higher the CPU usage, the more difficult it is to find the correct nonce for a block  
  
### Files:  
`launch.py`: sends appropriate files and launches the tracker process and node processes on their respective VMs. Logs the output of each process to the terminal. Kills launched processes when it receives a keyboard interrupt. Plays a role in testing (see testing.md for details).  
`block_chain.py`: defines node, block, and blockchain classes. A BlockChain object has methods to add blocks, validate blocks, and mine blocks. A BlockChain object is a linked list of nodes where each node contains a block. A Block object contains a nonce, some data, a previous hash, a hash, and an ID.  
`tracker.py`: the process to maintain a record of all the nodes in the network. It updates the list of nodes when a node joins or leaves.  
`node.py`: this program is run on each VM. It maintains a connection to the tracker and all other nodes. It mines blocks, verifies blocks, and updates its blockchain copy.  
`shop.py`: an application that utilizes our blockchain and network implementation to store records of transactions. It allows users to create accounts, buy monkeys, and switch between accounts. 
`visual.py`: the program to visualize the blockchain at a certain node. It periodically receives the blockchain from a node, parses the blockchain, puts the contents in a dictionary, and sends it to visual.js. The webpage reloads every time an updated blockchain is received.  
`long_chain.py`: test program that creates a long chain of blocks and sends the last block to a node in the network. The receiving node should request the long chain and replace its own chain with the longer one. This program can also be used to send a corrupt chain to see how the network handles it. See testing.md for usage information.  
`visual.css`, `visual.html`, `visual.js`:  visual.html is the webpage that displays the blockchain. visual.css styles the webpage. visual.js receives the blockchain from visual.py and is fed into visual.html. visual.py loads visual.html in a browser.

### Usage:  

First, create a firewall rule on google cloud. vm instances -> set up firewall rules -> create firewall rule -> name the rule, targets: all instances in the network,   source IP ranges: 0.0.0.0/0, protocols and ports: allow all, create.

SSH into each VM and install psutil:
$ sudo apt install python3-pip
$ pip install psutil

Run `launch.py`:  
$ python3 launch.py  
NOTICE: Run this process on your local machine. You have to install paramiko and scp. In addition, please change the values of global variables under 'vm configuration' to align with your own information.  
  
Run `shop.py`:  
python3 shop.py <tracker_port>  
NOTICE: make sure this program is running on the tracker VM. The tracker_port will be given to you at the top of the terminal output from launch.py.  
  
Run `visual.py`:  
python3 visual.py <node_ip> <node_port>  
NOTICE: run this program on your local machine in its own terminal. A node's IP and port will be given to you in the terminal output from launch.py. You must install selenium and change the path to your html file in visual.py to match its location on your machine. This path must be prepended with 'file://'. For example: 'file:///C:/Users/noaha/networks/project-degenerates/visual.html'. Graphics have been updated since our presentation.  
  
* interact with shop.py to see the blockchain visualization update in real-time  

05/08/2024
- added a note about the file path format under usage in README.md and added a comment about this in visual.py
- added docstrings to visual.py
- added a little more info to the shop behavior description in DESIGN.md under 'application'. Some wording was and spelling was fixed throughout DESIGN.md for clarity.