# WAV to RAW Converter for Teensy & ESP32

This repository provides a simple Python script and Batch file to convert audio files (WAV, MP3, FLAC, etc.) into RAW PCM format for use with Teensy 4.1, ESP32, and other microcontrollers.

## Features
- Batch processing – Converts all supported files in the folder.
- Supports multiple formats – WAV, MP3, FLAC, OGG, M4A, AAC, AIFF.
- Outputs RAW PCM – 16-bit, 44.1kHz, Mono (Teensy/ESP32-friendly).
- No dependencies beyond FFmpeg – Works on Windows, macOS, and Linux.

## Requirements
- **FFmpeg** (must be installed and added to PATH)
- **Python 3.x**
- `pydub` library (install via `pip install pydub`)

## Installation
### Windows
1. Install FFmpeg using Chocolatey:
   ```powershell
   choco install ffmpeg
