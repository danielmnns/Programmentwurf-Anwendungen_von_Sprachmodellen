let mediaRecorder;
let audioChunks = [];

document.addEventListener('DOMContentLoaded', () => {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const target = button.getAttribute('data-target');

            tabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            tabContents.forEach(content => {
                if (content.id === target) {
                    content.classList.add('active');
                } else {
                    content.classList.remove('active');
                }
            });
        });
    });
});

document.getElementById('record-button').addEventListener('click', async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    mediaRecorder.addEventListener('dataavailable', event => {
        audioChunks.push(event.data);
    });

    mediaRecorder.addEventListener('stop', () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        document.getElementById('audio-playback').src = audioUrl;

        const reader = new FileReader();
        reader.readAsDataURL(audioBlob);
        reader.onloadend = () => {
            document.getElementById('recorded-audio').value = reader.result;
            document.getElementById('submit-recording').disabled = false;
        };
    });

    document.getElementById('record-button').disabled = true;
    document.getElementById('stop-button').disabled = false;
});

document.getElementById('stop-button').addEventListener('click', () => {
    mediaRecorder.stop();
    document.getElementById('record-button').disabled = false;
    document.getElementById('stop-button').disabled = true;
});

async function handleFormSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    showLoading();
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    hideLoading();
    document.getElementById('transcription').innerText = result.transcription;
    document.getElementById('summary').innerText = result.summary;
}

document.getElementById('upload-form').addEventListener('submit', handleFormSubmit);
document.getElementById('record-form').addEventListener('submit', handleFormSubmit);

function showLoading() {
    document.getElementById('loading').style.display = 'block';
    let width = 0;
    const interval = setInterval(() => {
        if (width >= 100) {
            clearInterval(interval);
        } else {
            width++;
            document.getElementById('loading-bar').style.width = width + '%';
        }
    }, 100);
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
    document.getElementById('loading-bar').style.width = '0';
}S