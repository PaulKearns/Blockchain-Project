
const container = document.getElementById('container');

const items = {};

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

