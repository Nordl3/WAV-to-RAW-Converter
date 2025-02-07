WAV to RAW Converter for Teensy & ESP32 (Windows)

This repository provides a simple Python script and Batch file to convert audio files (WAV, MP3, FLAC, etc.) into RAW PCM format for use with Teensy 4.1, ESP32, and other microcontrollers.

## Features
- Converts all supported audio files in the folder.
- Supports WAV, MP3, FLAC, OGG, M4A, AAC, AIFF.
- Outputs RAW PCM – 16-bit, 44.1kHz, Mono (default) or Stereo (optional).
- No dependencies beyond FFmpeg – Runs with a simple batch file.

---

## Installation
### Step 1: Install FFmpeg
1. Open Command Prompt as Administrator and run:
   choco install ffmpeg

   If Chocolatey (choco) is not installed, install it first by following the instructions at:
   https://chocolatey.org/install

2. After installation, close and reopen Command Prompt.

3. Test that FFmpeg is installed by running:
   ffmpeg -version

   If FFmpeg is installed correctly, you will see version details.

---

### Step 2: Install Python
1. Download and install Python 3.x from:
   https://www.python.org/downloads/

2. During installation, check the box that says:
   Add Python to PATH

3. Verify Python is installed by running in Command Prompt:
   python --version

4. Install the required Python library:
   pip install pydub

---

## Usage

### Placing Files in the Folder
Place the following files in the same folder:
- convert_to_raw.py (Python script)
- convert_to_raw.bat (Batch file for easy execution)
- Your audio files (WAV, MP3, FLAC, etc.)

### Running the Conversion
#### Windows (Double Click)
- Double-click convert_to_raw.bat to process all audio files in the folder.

#### Windows (Command Line)
- Open a Command Prompt in the folder and run:
  python convert_to_raw.py

---

### Stereo or Mono Output
By default, the script converts all files to mono. This is recommended for Teensy and ESP32 to save memory.

#### How to Enable Stereo Output
If you want to keep stereo sound, modify the convert_to_raw.py file:

1. Open convert_to_raw.py in a text editor.
2. Find this line:
   "-ac", "1",  # Mono (default)
3. Change 1 to 2:
   "-ac", "2",  # Stereo
4. Save the file and run the script again.

---

## Output
- Converted .raw files will appear in the same folder as the originals.

---

## Technical Details
- Converts all audio files to:
  - 16-bit PCM
  - 44.1kHz sample rate
  - Mono (default) or Stereo (optional)
  - RAW format (s16le)
- Compatible with Teensy Audio Library, ESP32 I2S Audio, and other embedded systems.

---

## License
MIT License – Free to use, modify, and distribute.

---

## Future Plans
- Add a Python script to convert RAW to .h files for embedding in microcontrollers.
- Implement direct .wav -> .h conversion.
- Consider a GUI version.
