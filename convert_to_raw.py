import os
import subprocess

# Get the current folder where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Allowed input formats
AUDIO_EXTENSIONS = (".wav", ".mp3", ".flac", ".ogg", ".m4a", ".aiff", ".aac")

def convert_to_raw(input_file, output_file):
    """Convert audio file to 16-bit PCM RAW at 44.1kHz using FFmpeg."""
    command = [
        "ffmpeg", "-y",
        "-i", input_file,             # Input file
        "-ac", "1",                    # Mono (Teensy-friendly)
        "-ar", "44100",                 # 44.1kHz sample rate
        "-acodec", "pcm_s16le",         # 16-bit PCM little-endian
        "-f", "s16le",                  # RAW PCM format
        output_file
    ]
    
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Converted: {input_file} -> {output_file}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to convert: {input_file}")

# Process all audio files in the script's folder
for file_name in os.listdir(SCRIPT_DIR):
    if file_name.lower().endswith(AUDIO_EXTENSIONS):
        input_path = os.path.join(SCRIPT_DIR, file_name)
        output_path = os.path.join(SCRIPT_DIR, os.path.splitext(file_name)[0] + ".raw")
        
        # Skip if RAW file already exists
        if os.path.exists(output_path):
            print(f"⚠️ Skipping (already converted): {file_name}")
            continue
        
        convert_to_raw(input_path, output_path)

print("\n🎉 Conversion complete! RAW files are now in the same folder.")
