from selenium import webdriver
import time
import json
import socket
import sys
import pickle

js_data = {}
driver = webdriver.Chrome()


def generate_js():
    '''
    - generates the javascript code to be executed in the browser
    - the code will update the visualisation of the blockchain
    '''
    global js_data
    js_code = """
const container = document.getElementById('container');

const items = """ + json.dumps(js_data) + """;

function createPictureItem(src) {
    const itemDiv = document.createElement('div');
    itemDiv.classList.add('picture-item');

    const img = document.createElement('img');
    img.src = src;
    img.alt = 'Image';
    img.classList.add('picture');
    itemDiv.appendChild(img);

    return itemDiv;
}

function createValueItem(key, values) {
    const itemDiv = document.createElement('div');
    itemDiv.classList.add('value-item');

    const keyDiv = document.createElement('div');
    keyDiv.classList.add('key');
    keyDiv.textContent = key;
    itemDiv.appendChild(keyDiv);

    values.forEach(value => {
        const valueDiv = document.createElement('div');
        valueDiv.classList.add('value');
        valueDiv.textContent = value;
        itemDiv.appendChild(valueDiv);
    });

    return itemDiv;
}

Object.entries(items).forEach(([key, values], index) => {
    if (index === 0) {
        const valueItem = createValueItem(key, values);
        container.appendChild(valueItem);
    } else {
        const pictureItem = createPictureItem('chain.png');
        container.appendChild(pictureItem);

        const valueItem = createValueItem(key, values);
        container.appendChild(valueItem);
    }
});

"""

    with open('visual.js', 'w') as f:
        f.write(js_code)

    return js_code


def generate_html(driver):
    '''
    - generates the html code to be executed in the browser
    - the code will display the visualisation of the blockchain
    '''
    
    js_code = generate_js()

    driver.execute_script(js_code)

    driver.refresh()


def reload_html(driver):
    _ = generate_js()

    driver.refresh()



def visual(ip, port):
    '''
    - connects to the blockchain server
    - receives the blockchain
    - updates the visualisation
    '''

    global js_data
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    while True :

        new_data = {}

        data_buf = b''

        sock.sendall(b'D')

        data_length = int.from_bytes(sock.recv(4), 'big')

        while data_length:
            data = sock.recv(data_length)
            data_buf += data
            data_length -= len(data)

        data = pickle.loads(data_buf)


        n = data.header.next
        i = 1
        while n is not data.trailer:
            new_data[n.block.block_id] = [f"Nonce: {n.block.nonce}", f"Hash: {n.block.this_hash}", f"Prev Hash: {n.block.prev_hash}", f"{n.block.data}"]
            i += 1
            n = n.next
            
        if (new_data != js_data):
            js_data = new_data
            
            reload_html(driver)

        # time.sleep(1)

if __name__ == '__main__':
    ######## IMPORTANT ##############
    ######## EDIT PATH FOR LOCAL MACHINE ############
    ### Make sure to prepend the path with 'file://' ###
    driver.get(r"file:///C:/Users/noaha/networks/project-degenerates/visual.html")

    generate_html(driver)

    ip = sys.argv[1]

    port = int(sys.argv[2])

    visual(ip, port)
