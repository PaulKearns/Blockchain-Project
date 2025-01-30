import hashlib
import pickle
import psutil
import random
import datetime

class Block:
    def __init__(self, block_id, nonce, this_hash, prev_hash, data):
        '''
        - block_id: the unique identifier of the block
        - nonce: the number that is incremented to find a valid hash
        - this_hash: the hash of the block
        - prev_hash: the hash of the previous block
        - data: the data stored in the block'''
        self.block_id = block_id
        self.nonce = nonce
        self.this_hash = this_hash
        self.prev_hash = prev_hash
        self.data = data

class Node:
    def __init__(self, block):
        '''
        - block: the block stored in the node
        - next: the next node in the chain
        - prev: the previous node in the chain'''
        self.block = block
        self.next = None
        self.prev = None

class BlockChain:
    def __init__(self):
        '''
        - block_chain: a doubly linked list of blocks with sentinel nodes
        - header: the first node in the chain
        - trailer: the last node in the chain
        - length: the number of blocks in the chain
        '''
        self.header = Node(None)
        self.trailer = Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.length = 0

    def mine(self, data):
        '''
        - calculating the hash of the block
        - incrementing the nonce until the hash has three leading zeros
        - creating a new block with the data
        - adding the block to the chain
        '''
        if self.length == 0:
            prev_hash = '0'
        else:
            prev_hash = self.trailer.prev.block.this_hash
        block_id = self.length + 1
        nonce = 0
        combo = [nonce, block_id, prev_hash, data]
        this_hash = hashlib.sha256(pickle.dumps(combo)).hexdigest()

        probability = psutil.cpu_percent(interval=1)
        print(f'CPU usage: {probability}%')
        interrupts = 0

        # get the current time
        x = datetime.datetime.now()
        while this_hash[:3] != '000':

            if datetime.datetime.now() - x > datetime.timedelta(seconds=30):
                print('mining took too long')
                return 1

            nonce += 1
            combo[0] = nonce
            this_hash = hashlib.sha256(pickle.dumps(combo)).hexdigest()

            # Mining gets more difficult as CPU usage increases
            if probability > random.uniform(0, 100000):
                nonce /= 2
                interrupts += 1

        block = Block(block_id, nonce, this_hash, prev_hash, data)
        self.add(block)
        if interrupts:
            print(f'{interrupts} mining interrupts occurred')

    def validate(self, block):
        '''
        - checking if the block is the first block in the chain
        - checking if the previous hash matches the hash of the previous block
        - confirming the hash of the block
        - checking if the hash has three leading zeros
        - checking if the block id is one more than the previous block id
        '''
        if self.length == 0:
            if block.prev_hash != '0':
                return False
        elif self.trailer.prev.block.this_hash != block.prev_hash:
            return False
        combo = [block.nonce, block.block_id, block.prev_hash, block.data]
        this_hash = hashlib.sha256(pickle.dumps(combo)).hexdigest()
        if this_hash != block.this_hash:
            return False
        if this_hash[:3] != '000':
            return False
        if block.block_id != self.length + 1:
            return False
        return True
    
    def add(self, block):
        '''
        - creating a new node with the block
        - adding the node to the end of the chain
        '''
        node = Node(block)
        node.prev = self.trailer.prev
        node.next = self.trailer
        self.trailer.prev.next = node
        self.trailer.prev = node
        self.length += 1