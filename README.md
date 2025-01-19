# KI-gestütztes Meeting-Protokoll-Tool

## Inhaltsverzeichnis
1. [Projektbeschreibung](#1-projektbeschreibung)
2. [Systemsetup](#2-systemsetup)  
    2.1 [Voraussetzungen](#21-voraussetzungen))  
    2.2 [Installation](#22-installation)  
    2.3 [Häufige Fehler](#23-häufige-fehler)  
        2.3.1 [Fehler bei der Installation von `openai-whisper`](#231-fehler-bei-der-installation-von-openai-whisper)  
        2.3.2 [Fehler: `ffmpeg` nicht gefunden](#232-fehler-ffmpeg-nicht-gefunden)  
3. [Präsentation](#3-präsentation)
4. [Kontakt](#4-kontakt)


## 1. Projektbeschreibung
Unser Projekt bietet eine benutzerfreundliche Lösung zur Audioverarbeitung mit automatischer Transkription und Zusammenfassung. Das System ermöglicht es, Audioaufnahmen direkt aufzunehmen oder bestehende Dateien hochzuladen und in wenigen Schritten in Textform umzuwandeln. Dabei steht die einfache Bedienung und klare visuelle Rückmeldung im Vordergrund.

## 2. Systemsetup
### 2.1 Voraussetzungen

Stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind, bevor Sie mit der Installation fortfahren:

- Python 3.8 oder höher
- pip (Python Package Installer)


#### 2.1.1 Ollama 
OllamaSetup installieren: https://ollama.com/

##### 2.1.1.1 Ausführen
In der Powershell das Kommando
```ollama run llama3.2``` 
ausführen.

#### 2.1.2 Python 
Python installieren: https://www.python.org/

### 2.2 Installation
#### 2.2.1 Installation (Weg 1)
1. Entwicklungsumgebung erstellen
2. Öffnen Sie Ihre bevorzugte Entwicklungsumgebung oder einen Code-Editor wie Visual Studio Code (VS Code).
3. Python Environment Manager auswählen
4. Python Symbol im linken Menü
5. Bei Venv (virtuelle Umgebung) auf das „+“-Symbol klicken, um eine neue virtuelle Umgebung zu erstellen.
6. Die virtuelle Umgebung in einem Terminal öffnen, um sicherzustellen, dass alle Installationen dort durchgeführt werden.

#### 2.2.2 Installation (Weg 2)
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

#### 2.2.3 Installieren Sie die erforderlichen Pakete aus der `requirements.txt`:
```bash
pip install -r code/requirements.txt
```

#### 2.2.4 PyTorch aktualisieren
Folgen Sie diesen Schritten, um **torch** zu aktualisieren:

#### 2.2.5 Installation überprüfen:
```bash
pip show torch
pip install --upgrade torch
```

#### 2.2.6 Installieren und Konfigurieren von ffmpeg

##### 2.2.6.1 Schritt 1: ffmpeg herunterladen
Besuchen Sie die offizielle ffmpeg-Download-Seite: ffmpeg.org/download.

Wählen Sie unter "Get packages & executable files" das Paket für Windows aus.
Laden Sie das ZIP-Archiv herunter (z. B. ffmpeg-release-essentials.zip).

##### 2.2.6.2 Schritt 2: ffmpeg entpacken
Entpacken Sie den heruntergeladenen Ordner (z.B. ffmpeg-release-essentials).
Speichern Sie den entpackten Ordner an einem festen Ort, z.B. C:\ffmpeg.

##### 2.2.6.3 Schritt 3: ffmpeg zum Systempfad hinzufügen
Damit ffmpeg von jeder Eingabeaufforderung aus zugänglich ist, müssen Sie es zu den Systemvariablen hinzufügen:

Öffnen Sie die Systemsteuerung und gehen zu System und Sicherheit > System.
Klicken Sie auf Erweiterte Systemeinstellungen.
Im Fenster Systemeigenschaften klicken Sie auf den Tab Erweitert und dann auf Umgebungsvariablen.
Im Abschnitt Systemvariablen:
Suchen und wählen Sie den Eintrag Path aus und klicken auf Bearbeiten.
Fügen Sie den Pfad zum bin-Verzeichnis von ffmpeg hinzu, z.B. C:\ffmpeg\bin.
Klicken Sie auf OK und schließen Sie alle Fenster.

##### 2.2.6.4 Schritt 4: Installation überprüfen
Öffnen Sie eine neue Eingabeaufforderung und geben Sie ein:

```bash
ffmpeg -version
```
Wenn ffmpeg korrekt eingerichtet ist, sehen Sie die Versionsinformationen.

#### 2.2.7 Projekt ausführen
Nachdem torch aktualisiert und ffmpeg installiert sind, können Sie die Anwendung ausführen. 
```
python pfad/zu/ihrer_datei.py
```

### 2.3 Häufige Fehler
#### 2.3.1 Fehler bei der Installation von `openai-whisper`

**Beschreibung**: Dieser Fehler tritt auf, wenn das Paket `openai-whisper` nicht erfolgreich installiert werden kann.

**Lösung**:
1. Aktualisieren Sie `pip`:
    ```bash
    python -m pip install --upgrade pip
    ```
2. Installieren Sie `openai-whisper` separat:
    ```bash
    pip install openai-whisper
    ```
3. Wenn das Problem weiterhin besteht, versuchen Sie, das Paket direkt von GitHub zu installieren:
    ```bash
    pip install git+https://github.com/openai/whisper.git
    ```

#### 2.3.2 Fehler: `ffmpeg` nicht gefunden

**Beschreibung**: Dieser Fehler tritt auf, wenn `ffmpeg` nicht korrekt installiert oder nicht im PATH verfügbar ist.

**Lösung**:
1. Stellen Sie sicher, dass `ffmpeg` installiert ist. Befolgen Sie die Anweisungen in der [Systemsetup.md](Systemsetup.md).
2. Überprüfen Sie, ob `ffmpeg` im PATH verfügbar ist:
    ```bash
    ffmpeg -version
    ```
3. Wenn `ffmpeg` nicht gefunden wird, fügen Sie den Installationspfad von `ffmpeg` zu Ihrem PATH hinzu.

## 3. Präsentation
Die Projektpräsentation mit Beispielnutzung finden Sie hier: `organisatorisches\Endpräsentation.pptx`

## 4. Kontakt
Sollten Sie weiterhin Probleme mit der Anwendung oder Fragen haben, wenden Sie sich bitte per E-Mail an uns.

---
