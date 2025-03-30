function submitData() {
    let data = {
        name: document.getElementById('name').value,
        number: document.getElementById('number').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value
    };
    fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    }).then(response => response.json()).then(data => alert(data.message));
}

function fetchData() {
    fetch('/get').then(response => response.json()).then(data => {
        document.getElementById('dataDisplay').value = JSON.stringify(data, null, 2);
    });
}