document.getElementById('textForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const userInput = document.getElementById('userInput').value;
    const output = document.getElementById('output');

    try {
        const openaiResponse = await fetchOpenAIResponse(userInput);
        output.innerText = `You entered: ${openaiResponse}`;

        const speakButton = document.getElementById('speakButton');
        speakButton.style.display = 'inline';
        speakButton.onclick = function() {
            speakText(openaiResponse);
        };
    } catch (error) {
        console.error('Error:', error);
        output.innerText = 'An error occurred. Please try again.';
    }
});


async function speakText(text) {
    const response = await fetch('https://texttospeech.googleapis.com/v1/text:synthesize?key=YOUR_GOOGLE_CLOUD_API_KEY', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            input: { text },
            voice: { languageCode: 'en-US', ssmlGender: 'NEUTRAL' },
            audioConfig: { audioEncoding: 'MP3' }
        })
    });

    const data = await response.json();
    const audioContent = data.audioContent;
    const audio = new Audio(`data:audio/mp3;base64,${audioContent}`);
    audio.play();
}
