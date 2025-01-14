let mediaRecorder; // Variable zum Speichern des MediaRecorder-Objekts
let audioChunks = []; // Array zum Speichern der aufgezeichneten Audiodaten

// Event-Listener, um Funktionen nach dem Laden der Seite zu initialisieren
document.addEventListener("DOMContentLoaded", () => {
  // Tabs-Menü: Wechsel zwischen verschiedenen Inhalten
  const tabButtons = document.querySelectorAll(".tab-button");
  const tabContents = document.querySelectorAll(".tab-content");

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const target = button.getAttribute("data-target"); // Zielinhalt basierend auf 'data-target'

      // Aktiven Tab markieren und Inhalte wechseln
      tabButtons.forEach((btn) => btn.classList.remove("active"));
      button.classList.add("active");

      tabContents.forEach((content) => {
        content.classList.toggle("active", content.id === target); // Nur Zielinhalt anzeigen
      });
    });
  });

  // Datei-Upload-Funktionalität
  const fileInput = document.getElementById("audio-file");
  const uploadButton = document.getElementById("submit-upload");
  uploadButton.disabled = true; // Upload-Button standardmäßig deaktiviert

  fileInput.addEventListener("change", () => {
    uploadButton.disabled = fileInput.files.length === 0; // Aktivieren, wenn eine Datei ausgewählt wurde
  });

  // Aufnahmefunktionalität
  document
    .getElementById("record-button")
    .addEventListener("click", async () => {
      // Zugriff auf das Mikrofon des Nutzers
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream); // MediaRecorder-Objekt initialisieren
      mediaRecorder.start(); // Aufnahme starten

      mediaRecorder.addEventListener("dataavailable", (event) => {
        audioChunks.push(event.data); // Audio-Daten sammeln
      });

      mediaRecorder.addEventListener("stop", () => {
        // Audio-Daten in ein Blob-Objekt konvertieren und URL generieren
        const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
        const audioUrl = URL.createObjectURL(audioBlob);
        document.getElementById("audio-playback").src = audioUrl; // Wiedergabe-URL setzen

        // Base64-String erstellen und im Formular speichern
        const reader = new FileReader();
        reader.readAsDataURL(audioBlob);
        reader.onloadend = () => {
          document.getElementById("recorded-audio").value = reader.result;
          document.getElementById("submit-recording").disabled = false; // Aufnahme absenden aktivieren
        };
      });

      // Buttons für Aufnahme und Stopp anpassen
      document.getElementById("record-button").disabled = true;
      document.getElementById("stop-button").disabled = false;
    });

  // Stopp der Aufnahme
  document.getElementById("stop-button").addEventListener("click", () => {
    mediaRecorder.stop(); // Aufnahme beenden
    document.getElementById("record-button").disabled = false;
    document.getElementById("stop-button").disabled = true;
  });

  // Formular-Submit-Handler (für Datei-Upload und Audio-Aufnahme)
  async function handleFormSubmit(event) {
    event.preventDefault(); // Verhindert das Standardformularverhalten
    const formData = new FormData(event.target); // Formulardaten sammeln
    showLoading(); // Ladeanzeige aktivieren

    try {
      const response = await fetch("/upload", {
        // Daten an Server senden
        method: "POST",
        body: formData,
      });

      const result = await response.json(); // Serverantwort auslesen
      completeLoading(); // Ladeanzeige beenden

      // Ergebnisse anzeigen
      document.getElementById("transcription").innerText = result.transcription;
      document.getElementById("summary").innerText = result.summary;

      updateDownloadButtonState(); // PDF-Download-Button aktualisieren
    } catch (error) {
      hideLoading(); // Ladeanzeige ausblenden
      console.error("Error during upload:", error);
      alert("An error occurred. Please try again.");
    }
  }

  // Event-Listener für Formularabsendungen
  document
    .getElementById("upload-form")
    .addEventListener("submit", handleFormSubmit);
  document
    .getElementById("record-form")
    .addEventListener("submit", handleFormSubmit);

  // Ladeanzeige
  function showLoading() {
    document.getElementById("loading").style.display = "block"; // Ladeanzeige einblenden
    let width = 0;

    // Fortschrittsanimation simulieren
    const interval = setInterval(() => {
      if (width < 90) {
        width += Math.random() * 1.5; // Zufälliger Fortschritt
      }
      document.getElementById("loading-bar").style.width = width + "%";

      if (width >= 90) {
        clearInterval(interval); // Stopp bei 90 %
      }
    }, 200);
  }

  function completeLoading() {
    document.getElementById("loading-bar").style.width = "100%"; // Fortschritt auf 100 % setzen
    setTimeout(hideLoading, 500); // Ladeanzeige nach kurzer Zeit ausblenden
  }

  function hideLoading() {
    document.getElementById("loading").style.display = "none"; // Ladeanzeige ausblenden
  }

  // PDF-Download-Button aktivieren/deaktivieren
  function updateDownloadButtonState() {
    const transcription = document
      .getElementById("transcription")
      .innerText.trim();
    const summary = document.getElementById("summary").innerText.trim();
    const downloadButton = document.getElementById("download-pdf");

    downloadButton.disabled = !(transcription && summary); // Aktivieren, wenn beide Texte verfügbar sind
  }

  // PDF-Download-Funktion
  document.getElementById("download-pdf").addEventListener("click", () => {
    const transcription = document
      .getElementById("transcription")
      .innerText.trim();
    const summary = document.getElementById("summary").innerText.trim();

    if (transcription && summary) {
      const { jsPDF } = window.jspdf;
      const doc = new jsPDF();

      // Transcription-Seite
      doc.setFont("Helvetica", "bold");
      doc.setFontSize(16);
      doc.text("Transcription", 105, 20, { align: "center" });
      doc.setFont("Helvetica", "normal");
      doc.setFontSize(12);
      doc.text(transcription, 20, 30, { maxWidth: 170 });

      // Summary-Seite
      doc.addPage();
      doc.text("Summary", 105, 20, { align: "center" });
      doc.text(summary, 20, 30, { maxWidth: 170 });

      doc.save("Transcription_and_Summary.pdf"); // PDF speichern
    } else {
      alert("Transcription or Summary is missing.");
    }
  });
});
