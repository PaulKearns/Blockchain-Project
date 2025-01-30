# pip install paramiko
# pip install scp
# SSH into each vm prior to running this script
# Might need to delete entries from known_hosts for key mismatches

import random
from paramiko import SSHClient
from scp import SCPClient
import threading
import sys
import time
import signal
import os

def exit_sequence(sig, frame):
    '''
    - sending SIGINT to all node.py and tracker.py processes
    - exiting the script
    '''
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(tracker_ip, username=uni, key_filename=key_filename)
    _, tracker_run_stdout, _ = ssh.exec_command(
    f"stdbuf -oL pkill -SIGINT -f node.py")
    for line in tracker_run_stdout:
        print(f"VM  {tracker_ip} [tracker] {line.rstrip()}")
    ssh.close()
    for vm_ip in vm_node_ips:
        ssh.connect(vm_ip, username=uni, key_filename=key_filename)
        _, node_run_stdout, _ = ssh.exec_command(
        f"stdbuf -oL pkill -SIGINT -f node.py")
        for line in node_run_stdout:
            print(f"VM  {vm_ip} [node] {line.rstrip()}")
        ssh.close()
    os._exit(0)

# test1 or test2 can optionally be passed as an argument to the script
TEST1 = True if len(sys.argv) > 1 and sys.argv[1] == 'test1' else False
TEST2 = True if len(sys.argv) > 1 and sys.argv[1] == 'test2' else False

# vm configuration
uni = "nah2178" # put your UNI
key_filename = "C:/Users/noaha/.ssh/csee4119-s24" # replace with the ssh key path
tracker_ip = '34.42.241.158' # separate vm ip for tracker
vm_node_ips = ['104.155.179.22', '34.67.248.126', '34.41.173.214'] # node vm ips

port = random.randint(49152, 65535) # port to be used by tracker/shop VM
print(f'\nCommand to run shop.py:\npython3 shop.py {port}\n')

# colors work with up to 5 nodes and 1 tracker
vm_colors = {}
colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m',
          '\033[96m']
for node in vm_node_ips:
    vm_colors[node] = colors.pop()
vm_colors[tracker_ip] = colors.pop()


def load_files():
    """
    - sending tracker.py to tracker vm
    - sending node.py and block_chain.py to each node vm
    - sending shop.py and optionally long_chain.py to tracker vm
    """
    ssh = SSHClient() 
    ssh.load_system_host_keys()

    print('sending files to tracker and nodes...')

    # send relevant file to tracker
    ssh.connect(tracker_ip, username=uni, key_filename=key_filename)
    with SCPClient(ssh.get_transport()) as scp:
        scp.put('tracker.py', 'tracker.py')
        scp.put('shop.py', 'shop.py')
        if TEST1:
            print('\nCommand to run long_chain.py:\n' +
                  f'python3 long_chain.py {port} {tracker_ip}\n')
            scp.put('long_chain.py', 'long_chain.py')
            scp.put('block_chain.py', 'block_chain.py')
    ssh.close()

    # send relevant files to nodes
    for vm_node_ip in vm_node_ips:
        ssh.connect(vm_node_ip, username=uni, key_filename=key_filename)
        with SCPClient(ssh.get_transport()) as scp:
            scp.put('node.py', 'node.py')
            scp.put('block_chain.py', 'block_chain.py')
        ssh.close()

def start_tracker(vm_ip):
    """
    - starting tracker process in a given VM
    - printing any output of tracker.py process running on the VM to console
    """
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(vm_ip, username=uni, key_filename=key_filename)
    _, tracker_run_stdout, _ = ssh.exec_command(
        f"stdbuf -oL python3 -u tracker.py {port}&")
    for line in tracker_run_stdout:
        print(vm_colors[vm_ip] + f"VM  {vm_ip} [tracker] {line.rstrip()}" +
              vm_colors[vm_ip])
    ssh.close()

def start_node(vm_name, vm_ip):
    """
    - starting node process in a given VM
    - printing any output of node.py process running on the VM to console
    - restarting the node process if TEST2 is True
    """
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(vm_ip, username=uni, key_filename=key_filename)
    while True:
        _, node_run_stdout, _ = ssh.exec_command(
            f"stdbuf -oL python3 -u node.py " +
            f"{tracker_ip} {port} {vm_ip} &")
        
        for line in node_run_stdout:
            print(vm_colors[vm_ip] + f"VM  {vm_ip} [node{vm_name}]" +
                f"{line.rstrip()}" +
                vm_colors[vm_ip])
        if not TEST2:
            ssh.close()
            return
        input('Press enter to restart node\n')

def launch():
    """
    - starting tracker and node processes in separate threads
    - waiting 2 seconds before starting node processes to ensure tracker is up
    """
    threads = []

    # start tracker process
    t = threading.Thread(target=start_tracker, args=(tracker_ip,))
    t.start()
    threads.append(t)

    time.sleep(2)

    # start node process in each machine
    for vm_name, vm_ip in enumerate(vm_node_ips):
        t = threading.Thread(target=start_node, args=(vm_name + 1, vm_ip,))
        t.start()
        threads.append(t)
  

if __name__ == "__main__":
   signal.signal(signal.SIGINT, exit_sequence)
   load_files() # comment this out if you have already SCP'd the files
   launch()