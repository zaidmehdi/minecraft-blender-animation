document.getElementById("textForm").addEventListener("submit", function(event) {
    event.preventDefault();

    document.getElementById("loader").style.display = "block";

    var userInput = document.getElementById("userInput").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/animate");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            document.getElementById("loader").style.display = "none";
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                displayVideo(response.video_path);
            } else {
                console.error("Error:", xhr.status);
            }
        }
    };
    xhr.send(JSON.stringify({ text: userInput }));
});


function displayVideo(videoPath) {
    var videoPlayer = document.getElementById("videoPlayer");
    videoPlayer.src = videoPath;
    videoPlayer.controls = true;
    videoPlayer.autoplay = true;
}