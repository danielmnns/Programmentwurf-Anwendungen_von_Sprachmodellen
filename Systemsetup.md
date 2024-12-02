# Systemsetup

## Voraussetzungen

Stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind, bevor Sie mit der Installation fortfahren:

- Python 3.8 oder höher
- pip (Python Package Installer)

## Installation

Folgen Sie diesen Schritten, um die erforderlichen Pakete zu installieren:

1. Erstellen Sie eine virtuelle Umgebung:
    ```bash
    python -m venv Myenvi
    ```

2. Aktivieren Sie die virtuelle Umgebung:
    - Windows:
        ```bash
        Myenvi\Scripts\activate
        ```
    - macOS/Linux:
        ```bash
        source Myenvi/bin/activate
        ```

3. Installieren Sie die erforderlichen Pakete aus der `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## PyTorch aktualisieren

Folgen Sie diesen Schritten, um **torch** zu aktualisieren:

### Installation überprüfen:
```bash
pip show torch
pip install --upgrade torch
```

## Installieren und Konfigurieren von ffmpeg

### Schritt 1: ffmpeg herunterladen
Besuchen Sie die offizielle ffmpeg-Download-Seite: ffmpeg.org/download.

Wählen Sie unter "Get packages & executable files" das Paket für Windows aus.
Laden Sie das ZIP-Archiv herunter (z. B. ffmpeg-release-essentials.zip).

### Schritt 2: ffmpeg entpacken
Entpacken Sie den heruntergeladenen Ordner (z.B. ffmpeg-release-essentials).
Speichern Sie den entpackten Ordner an einem festen Ort, z.B. C:\ffmpeg.

### Schritt 3: ffmpeg zum Systempfad hinzufügen
Damit ffmpeg von jeder Eingabeaufforderung aus zugänglich ist, müssen Sie es zu den Systemvariablen hinzufügen:

Öffnen Sie die Systemsteuerung und gehen zu System und Sicherheit > System.
Klicken Sie auf Erweiterte Systemeinstellungen.
Im Fenster Systemeigenschaften klicken Sie auf den Tab Erweitert und dann auf Umgebungsvariablen.
Im Abschnitt Systemvariablen:
Suchen und wählen Sie den Eintrag Path aus und klicken auf Bearbeiten.
Fügen Sie den Pfad zum bin-Verzeichnis von ffmpeg hinzu, z.B. C:\ffmpeg\bin.
Klicken Sie auf OK und schließen Sie alle Fenster.

### Schritt 4: Installation überprüfen
Öffnen Sie eine neue Eingabeaufforderung und geben Sie ein:

```bash
ffmpeg -version
```
Wenn ffmpeg korrekt eingerichtet ist, sehen Sie die Versionsinformationen.

## Projekt ausführen
Nachdem torch aktualisiert und ffmpeg installiert sind, können Sie die Anwendung ausführen