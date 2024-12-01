// console.log('hello champ...thank you for being here')


document.addEventListener('DOMContentLoaded', function() {
    // Display a welcome message on the page
    const container = document.createElement('div');
    container.className = 'container';
    document.body.appendChild(container);

    const message = document.createElement('h1');
    message.textContent = 'Hello Champ! Thank you for being here.';
    container.appendChild(message);

    // Create a button that changes the background color when clicked
    const button = document.createElement('button');
    button.textContent = 'Change Background Color';
    container.appendChild(button);

    button.addEventListener('click', function() {
        // Toggle background color between green and blue
        if (document.body.style.backgroundColor === 'green') {
            document.body.style.backgroundColor = 'blue';
        } else {
            document.body.style.backgroundColor = 'green';
        }
    });

    console.log('hello champ...thank you for being here');
});
