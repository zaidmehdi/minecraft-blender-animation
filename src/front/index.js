document.getElementById("textForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var userInput = document.getElementById("userInput").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/animate");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                document.getElementById("output").innerText = response.message;
            } else {
                console.error("Error:", xhr.status);
            }
        }
    };
    xhr.send(JSON.stringify({ text: userInput }));
});