# TESTING

We will provide two tests in the following. The first test will verify that when a node receive an invalid block, it will reject it; and when a node receive a block that have lager block ID, it will request the whole new chain. The second test will verify that when a node joins or leaves the network, the whole network still behaves properly.  

For test 1, we do see that when a random node join the network and send an invalid block, the rest of the node will refuse it by doing nothing. When the random node mine 10 blocks and send it to a node, the rest of the node will start to request this longer block chains later. This is sufficent to show that our program can deal with invalid block or forked blockchain.  

For test 2, we do see that when firstly, a node leaves the network, the rest of the peers all behave normal. Then, when the node rejoin the network, all the nodes all behave as expected. This is sufficent to show that our program can deal with node joining and leaving.   
  
## TEST 1, Long Chain Domination/Chain & Block Validation:  
1. Run launch.py with three nodes and use 'test1' as cla.  
2. Run long_chain.py with launch.py output command and 'bad' as third cla on
tracker vm. Observe no chain update in contacted node due to corrupt chain in
launch.py output.  
3. Run shop.py on the tracker vm and update the record a few times (no more
than 5). See blocks being broadcast throughout the network from launch.py
output.  
4. Run long_chain.py with shop port as first cla on tracker vm in a different
terminal. Observe the contacted node's chain being overwritten with the valid
longer chain from launch.py output.  
5. Update the shop's record a few more times and notice that when the node with
the long chain is contacted, its chain overwrites the other chains in the
network. See this in launch.py's output.  
  
### Test 1 Shell Session:  

On local machine:  
/# python3 launch.py test1  

Command to run shop.py:  
python3 shop.py 49984  
  
sending files to tracker and nodes...  
  
Command to run long_chain.py:  
python3 long_chain.py 49984 34.42.241.158  

VM  34.42.241.158 [tracker] listening on port 49984  
VM  34.41.173.214 [node3]listening on port 49230  
VM  34.67.248.126 [node2]listening on port 59357  
VM  34.67.248.126 [node2]established connection with ('34.41.173.214', 49230)  
VM  34.41.173.214 [node3]established connection with 34.67.248.126  
VM  104.155.179.22 [node1]listening on port 63084  
VM  104.155.179.22 [node1]established connection with ('34.67.248.126', 59357)  
VM  34.67.248.126 [node2]established connection with 104.155.179.22  
VM  104.155.179.22 [node1]established connection with ('34.41.173.214', 49230)  
VM  34.41.173.214 [node3]established connection with 104.155.179.22  
VM  104.155.179.22 [node1]established connection with 34.41.173.214  
VM  34.41.173.214 [node3]established connection with ('104.155.179.22', 63084)  
VM  34.41.173.214 [node3]established connection with ('34.67.248.126', 59357)  
VM  34.67.248.126 [node2]established connection with 34.41.173.214  
VM  34.67.248.126 [node2]established connection with ('104.155.179.22', 63084)  
VM  104.155.179.22 [node1]established connection with 34.67.248.126  
VM  104.155.179.22 [node1]established connection with 34.42.241.158  
VM  34.41.173.214 [node3]established connection with 34.42.241.158  
VM  34.67.248.126 [node2]established connection with 34.42.241.158  
VM  34.67.248.126 [node2]established connection with ('34.42.241.158', 59289)  
VM  34.41.173.214 [node3]established connection with ('34.42.241.158', 59289)  
VM  104.155.179.22 [node1]established connection with ('34.42.241.158', 59289)  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 51266): B  
VM  34.67.248.126 [node2]sent chain request to ('34.42.241.158', 59289)  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 51266): C  
VM  34.67.248.126 [node2]got a bad chain from ('34.42.241.158', 51266)  
VM  104.155.179.22 [node1]received from ('34.42.241.158', 40892):  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 51266):  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 52664):  
VM  34.42.241.158 [tracker] removing 34.42.241.158:59289  
VM  34.41.173.214 [node3]removed connection with ('34.42.241.158', 59289)  
VM  34.67.248.126 [node2]removed connection with ('34.42.241.158', 59289)  
VM  104.155.179.22 [node1]removed connection with ('34.42.241.158', 59289)  
VM  104.155.179.22 [node1]established connection with 34.42.241.158  
VM  34.41.173.214 [node3]established connection with 34.42.241.158  
VM  34.67.248.126 [node2]established connection with 34.42.241.158  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 60726): A  
VM  34.41.173.214 [node3]CPU usage: 1.0%  
VM  34.67.248.126 [node2]received from ('34.41.173.214', 52826): B  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]sent to ('104.155.179.22', 63084)  
VM  104.155.179.22 [node1]received from ('34.41.173.214', 59312): B  
VM  34.41.173.214 [node3]sent to ('34.67.248.126', 59357)  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 36722): A  
VM  34.67.248.126 [node2]CPU usage: 0.5%  
VM  34.67.248.126 [node2]sent to ('34.41.173.214', 49230)  
VM  34.41.173.214 [node3]received from ('34.67.248.126', 42556): B  
VM  34.67.248.126 [node2]sent to ('104.155.179.22', 63084)  
VM  104.155.179.22 [node1]received from ('34.67.248.126', 35844): B  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 2: {'noah': [970, ['baboon']]}  
VM  104.155.179.22 [node1]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 60726): A  
VM  34.41.173.214 [node3]CPU usage: 0.5%  
VM  34.67.248.126 [node2]received from ('34.41.173.214', 52826): B  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]received from ('34.41.173.214', 59312): B  
VM  34.67.248.126 [node2]block 2: {'noah': [970, ['baboon']]}  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  104.155.179.22 [node1]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]sent to ('104.155.179.22', 63084)  
VM  104.155.179.22 [node1]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.41.173.214 [node3]sent to ('34.67.248.126', 59357)  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 60726): A  
VM  34.41.173.214 [node3]CPU usage: 0.5%  
VM  34.41.173.214 [node3]sent to ('104.155.179.22', 63084)  
VM  104.155.179.22 [node1]received from ('34.41.173.214', 59312): B  
VM  34.41.173.214 [node3]sent to ('34.67.248.126', 59357)  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]block 2: {'noah': [970, ['baboon']]}  
VM  104.155.179.22 [node1]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  104.155.179.22 [node1]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  34.67.248.126 [node2]received from ('34.41.173.214', 52826): B  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 2: {'noah': [970, ['baboon']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  34.41.173.214 [node3]established connection with 34.42.241.158  
VM  34.67.248.126 [node2]established connection with 34.42.241.158  
VM  104.155.179.22 [node1]established connection with 34.42.241.158  
VM  34.41.173.214 [node3]established connection with ('34.42.241.158', 55475)  
VM  34.67.248.126 [node2]established connection with ('34.42.241.158', 55475)  
VM  104.155.179.22 [node1]established connection with ('34.42.241.158', 55475)  
VM  104.155.179.22 [node1]received from ('34.42.241.158', 40166): B  
VM  104.155.179.22 [node1]sent chain request to ('34.42.241.158', 55475)  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]block 2: {'noah': [970, ['baboon']]}  
VM  104.155.179.22 [node1]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  104.155.179.22 [node1]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  104.155.179.22 [node1]received from ('34.42.241.158', 40166): C  
VM  104.155.179.22 [node1]block 1: Monkey 0  
VM  104.155.179.22 [node1]block 2: Monkey 1  
VM  104.155.179.22 [node1]block 3: Monkey 2  
VM  104.155.179.22 [node1]block 4: Monkey 3  
VM  104.155.179.22 [node1]block 5: Monkey 4  
VM  104.155.179.22 [node1]block 6: Monkey 5  
VM  104.155.179.22 [node1]block 7: Monkey 6  
VM  104.155.179.22 [node1]block 8: Monkey 7  
VM  104.155.179.22 [node1]block 9: Monkey 8  
VM  104.155.179.22 [node1]block 10: Monkey 9  
VM  104.155.179.22 [node1]block 11: Monkey 10  
VM  104.155.179.22 [node1]block 12: Monkey 11  
VM  104.155.179.22 [node1]block 13: Monkey 12  
VM  104.155.179.22 [node1]block 14: Monkey 13  
VM  104.155.179.22 [node1]block 15: Monkey 14  
VM  104.155.179.22 [node1]block 16: Monkey 15  
VM  104.155.179.22 [node1]block 17: Monkey 16  
VM  104.155.179.22 [node1]block 18: Monkey 17  
VM  104.155.179.22 [node1]block 19: Monkey 18  
VM  104.155.179.22 [node1]block 20: Monkey 19  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 47272):  
VM  104.155.179.22 [node1]received from ('34.42.241.158', 40166):  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 44558):  
VM  34.42.241.158 [tracker] removing 34.42.241.158:55475  
VM  34.67.248.126 [node2]removed connection with ('34.42.241.158', 55475)  
VM  34.41.173.214 [node3]removed connection with ('34.42.241.158', 55475)  
VM  104.155.179.22 [node1]removed connection with ('34.42.241.158', 55475)  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 60726): A  
VM  34.41.173.214 [node3]CPU usage: 0.0%  
VM  34.41.173.214 [node3]sent to ('104.155.179.22', 63084)  
VM  34.41.173.214 [node3]sent to ('34.67.248.126', 59357)  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [970, ['baboon']]}  
VM  34.67.248.126 [node2]received from ('34.41.173.214', 52826): B  
VM  34.41.173.214 [node3]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.41.173.214 [node3]block 5: {'noah': [660, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  104.155.179.22 [node1]received from ('34.41.173.214', 59312): B  
VM  34.67.248.126 [node2]block 5: {'noah': [660, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset']]}  
VM  104.155.179.22 [node1]block 1: Monkey 0  
VM  104.155.179.22 [node1]block 2: Monkey 1  
VM  104.155.179.22 [node1]block 3: Monkey 2  
VM  104.155.179.22 [node1]block 4: Monkey 3  
VM  104.155.179.22 [node1]block 5: Monkey 4  
VM  104.155.179.22 [node1]block 6: Monkey 5  
VM  104.155.179.22 [node1]block 7: Monkey 6  
VM  104.155.179.22 [node1]block 8: Monkey 7  
VM  104.155.179.22 [node1]block 9: Monkey 8  
VM  104.155.179.22 [node1]block 10: Monkey 9  
VM  104.155.179.22 [node1]block 11: Monkey 10  
VM  104.155.179.22 [node1]block 12: Monkey 11  
VM  104.155.179.22 [node1]block 13: Monkey 12  
VM  104.155.179.22 [node1]block 14: Monkey 13  
VM  104.155.179.22 [node1]block 15: Monkey 14  
VM  104.155.179.22 [node1]block 16: Monkey 15  
VM  104.155.179.22 [node1]block 17: Monkey 16  
VM  104.155.179.22 [node1]block 18: Monkey 17  
VM  104.155.179.22 [node1]block 19: Monkey 18  
VM  104.155.179.22 [node1]block 20: Monkey 19  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 36722): A  
VM  34.67.248.126 [node2]CPU usage: 0.5%  
VM  34.67.248.126 [node2]sent to ('34.41.173.214', 49230)  
VM  34.67.248.126 [node2]sent to ('104.155.179.22', 63084)  
VM  34.41.173.214 [node3]received from ('34.67.248.126', 42556): B  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  34.41.173.214 [node3]block 5: {'noah': [660, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset']]}  
VM  34.67.248.126 [node2]block 5: {'noah': [660, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset']]}  
VM  34.67.248.126 [node2]block 6: {'noah': [650, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset']]}       
VM  34.41.173.214 [node3]block 6: {'noah': [650, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset']]}       
VM  104.155.179.22 [node1]received from ('34.67.248.126', 35844): B  
VM  104.155.179.22 [node1]block 1: Monkey 0  
VM  104.155.179.22 [node1]block 2: Monkey 1  
VM  104.155.179.22 [node1]block 3: Monkey 2  
VM  104.155.179.22 [node1]block 4: Monkey 3  
VM  104.155.179.22 [node1]block 5: Monkey 4  
VM  104.155.179.22 [node1]block 6: Monkey 5  
VM  104.155.179.22 [node1]block 7: Monkey 6  
VM  104.155.179.22 [node1]block 8: Monkey 7  
VM  104.155.179.22 [node1]block 9: Monkey 8  
VM  104.155.179.22 [node1]block 10: Monkey 9  
VM  104.155.179.22 [node1]block 11: Monkey 10  
VM  104.155.179.22 [node1]block 12: Monkey 11  
VM  104.155.179.22 [node1]block 13: Monkey 12  
VM  104.155.179.22 [node1]block 14: Monkey 13  
VM  104.155.179.22 [node1]block 15: Monkey 14  
VM  104.155.179.22 [node1]block 16: Monkey 15  
VM  104.155.179.22 [node1]block 17: Monkey 16  
VM  104.155.179.22 [node1]block 18: Monkey 17  
VM  104.155.179.22 [node1]block 19: Monkey 18  
VM  104.155.179.22 [node1]block 20: Monkey 19  
VM  104.155.179.22 [node1]received from ('34.42.241.158', 47884): A  
VM  104.155.179.22 [node1]CPU usage: 0.5%  
VM  104.155.179.22 [node1]sent to ('34.67.248.126', 59357)  
VM  104.155.179.22 [node1]sent to ('34.41.173.214', 49230)  
VM  104.155.179.22 [node1]block 1: Monkey 0  
VM  104.155.179.22 [node1]block 2: Monkey 1  
VM  104.155.179.22 [node1]block 3: Monkey 2  
VM  104.155.179.22 [node1]block 4: Monkey 3  
VM  104.155.179.22 [node1]block 5: Monkey 4  
VM  104.155.179.22 [node1]block 6: Monkey 5  
VM  104.155.179.22 [node1]block 7: Monkey 6  
VM  104.155.179.22 [node1]block 8: Monkey 7  
VM  104.155.179.22 [node1]block 9: Monkey 8  
VM  34.67.248.126 [node2]received from ('104.155.179.22', 55006): B  
VM  104.155.179.22 [node1]block 10: Monkey 9  
VM  34.67.248.126 [node2]sent chain request to ('104.155.179.22', 63084)  
VM  34.41.173.214 [node3]received from ('104.155.179.22', 44382): B  
VM  34.41.173.214 [node3]sent chain request to ('104.155.179.22', 63084)  
VM  104.155.179.22 [node1]block 11: Monkey 10  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]block 12: Monkey 11  
VM  34.41.173.214 [node3]block 2: {'noah': [970, ['baboon']]}  
VM  104.155.179.22 [node1]block 13: Monkey 12  
VM  34.41.173.214 [node3]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  104.155.179.22 [node1]block 14: Monkey 13  
VM  34.41.173.214 [node3]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  104.155.179.22 [node1]block 15: Monkey 14  
VM  104.155.179.22 [node1]block 16: Monkey 15  
VM  104.155.179.22 [node1]block 17: Monkey 16  
VM  104.155.179.22 [node1]block 18: Monkey 17  
VM  34.41.173.214 [node3]block 5: {'noah': [660, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset']]}  
VM  104.155.179.22 [node1]block 19: Monkey 18  
VM  34.41.173.214 [node3]block 6: {'noah': [650, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset']]}       
VM  104.155.179.22 [node1]block 20: Monkey 19  
VM  104.155.179.22 [node1]block 21: {'noah': [640, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset', 'pygmy marmoset']]}  
VM  34.41.173.214 [node3]received from ('104.155.179.22', 44382): C  
VM  104.155.179.22 [node1]received from ('34.67.248.126', 35844): D  
VM  104.155.179.22 [node1]got chain request  
VM  34.41.173.214 [node3]block 1: Monkey 0  
VM  104.155.179.22 [node1]send_chain  
VM  34.41.173.214 [node3]block 2: Monkey 1  
VM  104.155.179.22 [node1]received from ('34.41.173.214', 59312): D  
VM  104.155.179.22 [node1]got chain request  
VM  34.41.173.214 [node3]block 3: Monkey 2  
VM  104.155.179.22 [node1]send_chain  
VM  104.155.179.22 [node1]sent chain to ('34.41.173.214', 49230) upon request  
VM  104.155.179.22 [node1]sent chain to ('34.67.248.126', 59357) upon request  
VM  34.41.173.214 [node3]block 4: Monkey 3  
VM  34.67.248.126 [node2]block 2: {'noah': [970, ['baboon']]}  
VM  34.41.173.214 [node3]block 5: Monkey 4  
VM  34.67.248.126 [node2]block 3: {'noah': [770, ['baboon', 'gorilla']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [670, ['baboon', 'gorilla', 'orangutan']]}  
VM  34.67.248.126 [node2]block 5: {'noah': [660, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset']]}  
VM  34.67.248.126 [node2]block 6: {'noah': [650, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset']]}       
VM  34.41.173.214 [node3]block 6: Monkey 5  
VM  34.67.248.126 [node2]received from ('104.155.179.22', 55006): C  
VM  34.41.173.214 [node3]block 7: Monkey 6  
VM  34.67.248.126 [node2]block 1: Monkey 0  
VM  34.41.173.214 [node3]block 8: Monkey 7  
VM  34.67.248.126 [node2]block 2: Monkey 1  
VM  34.41.173.214 [node3]block 9: Monkey 8  
VM  34.67.248.126 [node2]block 3: Monkey 2  
VM  34.41.173.214 [node3]block 10: Monkey 9  
VM  34.67.248.126 [node2]block 4: Monkey 3  
VM  34.41.173.214 [node3]block 11: Monkey 10  
VM  34.41.173.214 [node3]block 12: Monkey 11  
VM  34.67.248.126 [node2]block 5: Monkey 4  
VM  34.41.173.214 [node3]block 13: Monkey 12  
VM  34.67.248.126 [node2]block 6: Monkey 5  
VM  34.41.173.214 [node3]block 14: Monkey 13  
VM  34.67.248.126 [node2]block 7: Monkey 6  
VM  34.41.173.214 [node3]block 15: Monkey 14  
VM  34.67.248.126 [node2]block 8: Monkey 7  
VM  34.41.173.214 [node3]block 16: Monkey 15  
VM  34.67.248.126 [node2]block 9: Monkey 8  
VM  34.41.173.214 [node3]block 17: Monkey 16  
VM  34.67.248.126 [node2]block 10: Monkey 9  
VM  34.41.173.214 [node3]block 18: Monkey 17  
VM  34.67.248.126 [node2]block 11: Monkey 10  
VM  34.41.173.214 [node3]block 19: Monkey 18  
VM  34.67.248.126 [node2]block 12: Monkey 11  
VM  34.41.173.214 [node3]block 20: Monkey 19  
VM  34.67.248.126 [node2]block 13: Monkey 12  
VM  34.41.173.214 [node3]block 21: {'noah': [640, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset', 'pygmy marmoset']]}  
VM  34.67.248.126 [node2]block 14: Monkey 13  
VM  34.67.248.126 [node2]block 15: Monkey 14  
VM  34.67.248.126 [node2]block 16: Monkey 15  
VM  34.67.248.126 [node2]block 17: Monkey 16  
VM  34.67.248.126 [node2]block 18: Monkey 17  
VM  34.67.248.126 [node2]block 19: Monkey 18  
VM  34.67.248.126 [node2]block 20: Monkey 19  
VM  34.67.248.126 [node2]block 21: {'noah': [640, ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset', 'pygmy marmoset']]}  
  
### On tracker vm (terminal 1):  
/# python3 long_chain.py 49984 34.42.241.158 bad  
CPU usage: 1.0%  
CPU usage: 1.0%  
CPU usage: 0.5%  
CPU usage: 0.0%  
CPU usage: 0.0%  
CPU usage: 1.0%  
CPU usage: 0.0%  
CPU usage: 0.0%  
CPU usage: 1.5%  
CPU usage: 0.0%  
CPU usage: 0.5%  
CPU usage: 1.0%  
CPU usage: 1.0%  
CPU usage: 0.0%  
CPU usage: 1.0%  
CPU usage: 0.5%  
CPU usage: 0.0%  
CPU usage: 1.0%  
CPU usage: 0.5%  
CPU usage: 0.5%  
listening on 59289  
established connection with 34.67.248.126  
established connection with 34.41.173.214  
established connection with 104.155.179.22  
sent block to random node: ('34.67.248.126', 59357)  
got chain request  
sent chain to ('34.67.248.126', 59357) upon request  
^Cexiting  
  
/# python3 shop.py 49984  
What is your name? noah  
Updating record in blockchain at ('34.41.173.214', 49230)  
Welcome to the 🦧 shop, noah!  
Here is what we have for sale:  
1. baboon 🦧30 https://en.wikipedia.org/wiki/Papio  
2. gorilla 🦧200 https://en.wikipedia.org/wiki/Gorilla  
3. orangutan 🦧100 https://en.wikipedia.org/wiki/Orangutan  
4. chimpanzee 🦧50 https://en.wikipedia.org/wiki/Chimpanzee  
5. howler monkey 🦧10 https://en.wikipedia.org/wiki/Howler_monkey  
6. spider monkey 🦧10 https://en.wikipedia.org/wiki/Spider_monkey  
7. atlantic forest titi monkey 🦧69 https://en.wikipedia.org/wiki/Callicebus  
8. squirrel monkey 🦧10 https://en.wikipedia.org/wiki/Squirrel_monkey  
9. pygmy marmoset 🦧10 https://en.wikipedia.org/wiki/Pygmy_marmoset  
10. woolly monkey 🦧420 https://en.wikipedia.org/wiki/Lagothrix  
Balance: 1000  
Cart: []  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 1  
Updating record in blockchain at ('34.67.248.126', 59357)  
You have purchased a baboon!  
Balance: 970  
Cart: ['baboon']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 2  
Updating record in blockchain at ('34.41.173.214', 49230)  
You have purchased a gorilla!  
Balance: 770  
Cart: ['baboon', 'gorilla']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 3  
Updating record in blockchain at ('34.41.173.214', 49230)  
You have purchased a orangutan!  
Balance: 670  
Cart: ['baboon', 'gorilla', 'orangutan']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 9  
Updating record in blockchain at ('34.41.173.214', 49230)  
You have purchased a pygmy marmoset!  
Balance: 660  
Cart: ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 9  
Updating record in blockchain at ('34.67.248.126', 59357)  
You have purchased a pygmy marmoset!  
Balance: 650  
Cart: ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 9  
Updating record in blockchain at ('104.155.179.22', 63084)  
You have purchased a pygmy marmoset!  
Balance: 640  
Cart: ['baboon', 'gorilla', 'orangutan', 'pygmy marmoset', 'pygmy marmoset', 'pygmy marmoset']  
Enter p for purchase or n for new shopper:  
  
  
  
### On tracker vm (terminal 2):  
python3 long_chain.py 49984 34.42.241.158  
CPU usage: 0.5%  
CPU usage: 0.5%  
CPU usage: 0.0%  
CPU usage: 1.0%  
CPU usage: 1.5%  
CPU usage: 1.0%  
CPU usage: 0.5%  
CPU usage: 1.0%  
CPU usage: 0.0%  
CPU usage: 1.0%  
CPU usage: 0.0%  
CPU usage: 0.5%  
CPU usage: 0.5%  
CPU usage: 0.5%  
CPU usage: 0.5%  
CPU usage: 2.0%  
CPU usage: 1.0%  
CPU usage: 0.5%  
CPU usage: 0.0%  
CPU usage: 1.5%  
listening on 55475  
established connection with 34.67.248.126  
established connection with 34.41.173.214  
established connection with 104.155.179.22  
sent block to random node: ('104.155.179.22', 63084)  
got chain request  
sent chain to ('104.155.179.22', 63084) upon request  
^Cexiting  
  
## TEST 2, Node Leave & Join: 
1. Run launch.py with three nodes and use 'test2' as cla.  
2. Run shop.py on the tracker vm and update the record a few times. See blocks  
being broadcast throughout the network from launch.py output.  
4. SSH into one of the vms a node is running on.  
5. On that machine, send a SIGINT to node.py  
6. Update the shop record more and observe that activity is on only the  
remaining two nodes.  
6. Press enter in launch.py terminal to restart killed node.  
7. Update the shop record more and observe that activity is restored to three  
nodes.  
  
### On local machine:  
/# python3 launch.py test2  
  
Command to run shop.py:  
python3 shop.py 55253  
  
sending files to tracker and nodes...  
VM  34.42.241.158 [tracker] listening on port 55253  
VM  34.67.248.126 [node2]listening on port 61380  
VM  104.155.179.22 [node1]listening on port 56885  
VM  104.155.179.22 [node1]established connection with ('34.67.248.126', 61380)  
VM  34.67.248.126 [node2]established connection with 104.155.179.22  
VM  34.41.173.214 [node3]listening on port 61801  
VM  34.41.173.214 [node3]established connection with ('104.155.179.22', 56885)  
VM  34.67.248.126 [node2]established connection with 34.41.173.214  
VM  34.41.173.214 [node3]established connection with ('34.67.248.126', 61380)  
VM  104.155.179.22 [node1]established connection with 34.41.173.214  
VM  34.67.248.126 [node2]established connection with ('34.41.173.214', 61801)  
VM  34.67.248.126 [node2]established connection with ('104.155.179.22', 56885)  
VM  34.41.173.214 [node3]established connection with 34.67.248.126  
VM  104.155.179.22 [node1]established connection with 34.67.248.126  
VM  104.155.179.22 [node1]established connection with ('34.41.173.214', 61801)  
VM  34.41.173.214 [node3]established connection with 104.155.179.22  
VM  34.67.248.126 [node2]established connection with 34.42.241.158  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 48968): A  
VM  34.41.173.214 [node3]established connection with 34.42.241.158  
VM  104.155.179.22 [node1]established connection with 34.42.241.158  
VM  34.67.248.126 [node2]CPU usage: 1.0%  
VM  34.67.248.126 [node2]sent to ('34.41.173.214', 61801)  
VM  104.155.179.22 [node1]received from ('34.67.248.126', 34534): B  
VM  34.41.173.214 [node3]received from ('34.67.248.126', 44998): B  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]sent to ('104.155.179.22', 56885)  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 48968): A  
VM  34.67.248.126 [node2]CPU usage: 1.0%  
VM  34.67.248.126 [node2]sent to ('34.41.173.214', 61801)  
VM  34.67.248.126 [node2]sent to ('104.155.179.22', 56885)  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]received from ('34.67.248.126', 34534): B  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]received from ('34.67.248.126', 44998): B  
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 44350): A  
VM  34.41.173.214 [node3]CPU usage: 0.5%  
VM  34.41.173.214 [node3]sent to ('104.155.179.22', 56885)  
VM  34.41.173.214 [node3]sent to ('34.67.248.126', 61380)  
VM  104.155.179.22 [node1]received from ('34.41.173.214', 49432): B  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  104.155.179.22 [node1]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  104.155.179.22 [node1]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]received from ('34.41.173.214', 35322): B  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  104.155.179.22 [node1]received from ('34.42.241.158', 41456): A  
VM  34.67.248.126 [node2]received from ('104.155.179.22', 46686): B  
VM  104.155.179.22 [node1]CPU usage: 0.0%  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]sent to ('34.67.248.126', 61380)  
VM  104.155.179.22 [node1]sent to ('34.41.173.214', 61801)  
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]received from ('104.155.179.22', 57808): B  
VM  104.155.179.22 [node1]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  104.155.179.22 [node1]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  104.155.179.22 [node1]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 48968): A  
VM  34.67.248.126 [node2]CPU usage: 0.5%  
VM  34.67.248.126 [node2]1 mining interrupts occurred  
VM  34.67.248.126 [node2]sent to ('34.41.173.214', 61801)  
VM  34.67.248.126 [node2]sent to ('104.155.179.22', 56885)  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.41.173.214 [node3]received from ('34.67.248.126', 44998): B  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  104.155.179.22 [node1]received from ('34.67.248.126', 34534): B  
VM  34.41.173.214 [node3]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  104.155.179.22 [node1]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  104.155.179.22 [node1]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  104.155.179.22 [node1]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  104.155.179.22 [node1]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  104.155.179.22 [node1]exiting  
VM  34.42.241.158 [tracker] removing 104.155.179.22:56885  
VM  34.41.173.214 [node3]received from ('104.155.179.22', 57808):  
VM  34.67.248.126 [node2]received from ('104.155.179.22', 46686):  
Press enter to restart nodeVM  34.67.248.126 [node2]removed connection with ('104.155.179.22', 56885)  
VM  34.41.173.214 [node3]removed connection with ('104.155.179.22', 56885)  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 44350): A  
VM  34.41.173.214 [node3]CPU usage: 0.5%  
VM  34.41.173.214 [node3]sent to ('34.67.248.126', 61380)  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]received from ('34.41.173.214', 35322): B  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.41.173.214 [node3]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.67.248.126 [node2]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.41.173.214 [node3]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  34.67.248.126 [node2]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  34.41.173.214 [node3]received from ('34.42.241.158', 44350): A  
VM  34.41.173.214 [node3]CPU usage: 0.0%  
VM  34.67.248.126 [node2]received from ('34.41.173.214', 35322): B  
VM  34.41.173.214 [node3]sent to ('34.67.248.126', 61380)  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.41.173.214 [node3]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.67.248.126 [node2]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.41.173.214 [node3]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  34.67.248.126 [node2]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  34.41.173.214 [node3]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  34.67.248.126 [node2]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 48968): A  
VM  34.67.248.126 [node2]CPU usage: 0.0%  
VM  34.41.173.214 [node3]received from ('34.67.248.126', 44998): B  
VM  34.67.248.126 [node2]sent to ('34.41.173.214', 61801)  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.67.248.126 [node2]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.67.248.126 [node2]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  34.41.173.214 [node3]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.67.248.126 [node2]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  34.41.173.214 [node3]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  34.67.248.126 [node2]block 8: {'noah': [200, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']]}  
VM  34.41.173.214 [node3]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  34.41.173.214 [node3]block 8: {'noah': [200, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']]}  
  
VM  104.155.179.22 [node1]listening on port 63757  
VM  104.155.179.22 [node1]established connection with ('34.67.248.126', 61380)  
VM  104.155.179.22 [node1]established connection with ('34.41.173.214', 61801)  
VM  34.41.173.214 [node3]established connection with 104.155.179.22  
VM  34.67.248.126 [node2]established connection with 104.155.179.22  
VM  104.155.179.22 [node1]established connection with 34.67.248.126  
VM  34.67.248.126 [node2]established connection with ('104.155.179.22', 63757)  
VM  34.41.173.214 [node3]established connection with ('104.155.179.22', 63757)  
VM  104.155.179.22 [node1]established connection with 34.41.173.214  
VM  104.155.179.22 [node1]established connection with 34.42.241.158  
VM  34.67.248.126 [node2]received from ('34.42.241.158', 48968): A  
VM  34.67.248.126 [node2]CPU usage: 1.5%  
VM  34.67.248.126 [node2]sent to ('34.41.173.214', 61801)  
VM  34.67.248.126 [node2]sent to ('104.155.179.22', 63757)  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]received from ('34.67.248.126', 51904): B  
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.67.248.126 [node2]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  104.155.179.22 [node1]sent chain request to ('34.67.248.126', 61380)  
VM  34.67.248.126 [node2]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  104.155.179.22 [node1]received from ('34.67.248.126', 51904): C  
VM  34.67.248.126 [node2]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  34.67.248.126 [node2]block 8: {'noah': [200, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']]}  
VM  34.67.248.126 [node2]block 9: {'noah': [190, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset']]}  
VM  34.67.248.126 [node2]received from ('104.155.179.22', 52166): D  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.67.248.126 [node2]got chain request  
VM  34.67.248.126 [node2]send_chain  
VM  34.41.173.214 [node3]received from ('34.67.248.126', 44998): B  
VM  34.67.248.126 [node2]sent chain to ('104.155.179.22', 63757) upon request  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  104.155.179.22 [node1]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.41.173.214 [node3]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  104.155.179.22 [node1]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  104.155.179.22 [node1]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.41.173.214 [node3]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  104.155.179.22 [node1]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}  
VM  34.41.173.214 [node3]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  104.155.179.22 [node1]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  34.41.173.214 [node3]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  104.155.179.22 [node1]block 8: {'noah': [200, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']]}  
VM  34.41.173.214 [node3]block 8: {'noah': [200, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']]}  
VM  104.155.179.22 [node1]block 9: {'noah': [190, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset']]}  
VM  34.41.173.214 [node3]block 9: {'noah': [190, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset']]}  
VM  34.41.173.214 [node3]received from ('34.42.241.158', 44350): A  
VM  34.41.173.214 [node3]CPU usage: 0.0%  
VM  34.41.173.214 [node3]sent to ('34.67.248.126', 61380)  
VM  34.41.173.214 [node3]sent to ('104.155.179.22', 63757)  
VM  34.67.248.126 [node2]received from ('34.41.173.214', 35322): B  
VM  34.41.173.214 [node3]block 1: {'noah': [1000, []]}  
VM  104.155.179.22 [node1]received from ('34.41.173.214', 50030): B  
VM  34.41.173.214 [node3]block 2: {'noah': [990, ['howler monkey']]}  
VM  104.155.179.22 [node1]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  104.155.179.22 [node1]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.41.173.214 [node3]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.67.248.126 [node2]block 1: {'noah': [1000, []]}  
VM  34.41.173.214 [node3]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  34.67.248.126 [node2]block 2: {'noah': [990, ['howler monkey']]}  
VM  34.41.173.214 [node3]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  34.67.248.126 [node2]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.41.173.214 [node3]block 8: {'noah': [200, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']]}  
VM  34.67.248.126 [node2]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  34.41.173.214 [node3]block 9: {'noah': [190, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset']]}  
VM  34.67.248.126 [node2]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.41.173.214 [node3]block 10: {'noah': [180, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset', 'pygmy marmoset']]}  
VM  34.67.248.126 [node2]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}   
VM  104.155.179.22 [node1]block 3: {'noah': [940, ['howler monkey', 'chimpanzee']]}  
VM  34.67.248.126 [node2]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  104.155.179.22 [node1]block 4: {'noah': [740, ['howler monkey', 'chimpanzee', 'gorilla']]}  
VM  104.155.179.22 [node1]block 5: {'noah': [730, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']]}  
VM  34.67.248.126 [node2]block 8: {'noah': [200, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']]}  
VM  104.155.179.22 [node1]block 6: {'noah': [630, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']]}  
VM  34.67.248.126 [node2]block 9: {'noah': [190, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset']]}  
VM  104.155.179.22 [node1]block 7: {'noah': [210, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']]}  
VM  34.67.248.126 [node2]block 10: {'noah': [180, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset', 'pygmy marmoset']]}  
VM  104.155.179.22 [node1]block 8: {'noah': [200, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']]}  
VM  104.155.179.22 [node1]block 9: {'noah': [190, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset']]}  
VM  104.155.179.22 [node1]block 10: {'noah': [180, ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset', 'pygmy marmoset']]}  
  
### On tracker vm (terminal 1):  
/# python3 shop.py 55253  
What is your name? noah  
Updating record in blockchain at ('34.67.248.126', 61380)  
Welcome to the 🦧 shop, noah!  
Here is what we have for sale:  
1. baboon 🦧30 https://en.wikipedia.org/wiki/Papio  
2. gorilla 🦧200 https://en.wikipedia.org/wiki/Gorilla  
3. orangutan 🦧100 https://en.wikipedia.org/wiki/Orangutan  
4. chimpanzee 🦧50 https://en.wikipedia.org/wiki/Chimpanzee  
5. howler monkey 🦧10 https://en.wikipedia.org/wiki/Howler_monkey  
6. spider monkey 🦧10 https://en.wikipedia.org/wiki/Spider_monkey  
7. atlantic forest titi monkey 🦧69 https://en.wikipedia.org/wiki/Callicebus  
8. squirrel monkey 🦧10 https://en.wikipedia.org/wiki/Squirrel_monkey  
9. pygmy marmoset 🦧10 https://en.wikipedia.org/wiki/Pygmy_marmoset  
10. woolly monkey 🦧420 https://en.wikipedia.org/wiki/Lagothrix  
Balance: 1000  
Cart: []  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 5  
Updating record in blockchain at ('34.67.248.126', 61380)  
You have purchased a howler monkey!  
Balance: 990  
Cart: ['howler monkey']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 4  
Updating record in blockchain at ('34.41.173.214', 61801)  
You have purchased a chimpanzee!  
Balance: 940  
Cart: ['howler monkey', 'chimpanzee']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 2  
Updating record in blockchain at ('104.155.179.22', 56885)  
You have purchased a gorilla!  
Balance: 740  
Cart: ['howler monkey', 'chimpanzee', 'gorilla']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 8  
Updating record in blockchain at ('34.67.248.126', 61380)  
You have purchased a squirrel monkey!  
Balance: 730  
Cart: ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 3  
Removed connection with ('104.155.179.22', 56885)  
Updating record in blockchain at ('34.41.173.214', 61801)  
You have purchased a orangutan!  
Balance: 630  
Cart: ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 10  
Updating record in blockchain at ('34.41.173.214', 61801)  
You have purchased a woolly monkey!  
Balance: 210  
Cart: ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 6  
Updating record in blockchain at ('34.67.248.126', 61380)  
You have purchased a spider monkey!  
Balance: 200  
Cart: ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']  
Enter p for purchase or n for new shopper: p 9  
Invalid input. Please try again.  
Balance: 200  
Cart: ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 9  
Updating record in blockchain at ('34.67.248.126', 61380)  
You have purchased a pygmy marmoset!  
Balance: 190  
Cart: ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset']  
Enter p for purchase or n for new shopper: p  
Which item # would you like to purchase? 9  
Updating record in blockchain at ('34.41.173.214', 61801)  
You have purchased a pygmy marmoset!  
Balance: 180  
Cart: ['howler monkey', 'chimpanzee', 'gorilla', 'squirrel monkey', 'orangutan', 'woolly monkey', 'spider monkey', 'pygmy marmoset', 'pygmy marmoset']  
Enter p for purchase or n for new shopper:  
  
### On node vm:  
/# pkill -SIGINT -f node.py