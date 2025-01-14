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

    // Datei-Upload-Button
    const fileInput = document.getElementById('audio-file');
    const uploadButton = document.getElementById('submit-upload');

    // Standardmäßig deaktivieren
    uploadButton.disabled = true;

    // Event-Listener für Datei-Auswahl
    fileInput.addEventListener('change', () => {
        uploadButton.disabled = fileInput.files.length === 0;
    });

    // Record-Funktionalität
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

    // Formularabsendung (für Upload und Aufnahme)
    async function handleFormSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        showLoading();

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            completeLoading();

            // Ergebnisse anzeigen
            document.getElementById('transcription').innerText = result.transcription;
            document.getElementById('summary').innerText = result.summary;

            // Button-Status aktualisieren
            updateDownloadButtonState();
        } catch (error) {
            hideLoading();
            console.error('Error during upload:', error);
            alert('An error occurred. Please try again.');
        }
    }

    // Event-Listener für beide Formulare
    document.getElementById('upload-form').addEventListener('submit', handleFormSubmit);
    document.getElementById('record-form').addEventListener('submit', handleFormSubmit);

    // Ladeanzeige
    function showLoading() {
        document.getElementById('loading').style.display = 'block';
        let width = 0;

        // Fortschrittsanimation
        const interval = setInterval(() => {
            if (width < 90) {
                width += Math.random() * 1.5; // Zufälliger langsamer Fortschritt bis 90 %
            }
            document.getElementById('loading-bar').style.width = width + '%';

            if (width >= 90) {
                clearInterval(interval); // Stopp bei 90 %, bis die Serverantwort kommt
            }
        }, 200);
    }

    function completeLoading() {
        document.getElementById('loading-bar').style.width = '100%';
        setTimeout(() => {
            hideLoading();
        }, 500);
    }

    function hideLoading() {
        document.getElementById('loading').style.display = 'none';
    }

    function updateDownloadButtonState() {
        const transcription = document.getElementById('transcription').innerText.trim();
        const summary = document.getElementById('summary').innerText.trim();
        const downloadButton = document.getElementById('download-pdf');

        // Button aktivieren, wenn beide Inhalte verfügbar sind
        downloadButton.disabled = !(transcription && summary);
    }

    document.getElementById('download-pdf').addEventListener('click', () => {
        const transcription = document.getElementById('transcription').innerText;
        const summary = document.getElementById('summary').innerText;

        const doc = new jsPDF();
        doc.setFontSize(16);
        doc.text("Transcription", 10, 10);
        doc.setFontSize(12);
        doc.text(transcription, 10, 20);

        doc.setFontSize(16);
        doc.text("Summary", 10, 40);
        doc.setFontSize(12);
        doc.text(summary, 10, 50);

        doc.save("Transcription_and_Summary.pdf");
    });
})