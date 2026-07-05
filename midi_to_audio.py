import subprocess
import os
from pydub import AudioSegment

AudioSegment.converter = r"C:\Users\OSAMA DON\Downloads\ffmpeg-8.1.2-essentials_build\ffmpeg-8.1.2-essentials_build\bin\ffmpeg.exe"
from pydub import AudioSegment

# ============================
# PATHS
# ============================

soundfont = r"C:\Users\OSAMA DON\Downloads\GeneralUser_GS_v2.0.3--doc_r6\GeneralUser-GS\GeneralUser-GS.sf2"

midi_file = "generated_music.mid"

os.makedirs("static", exist_ok=True)

wav_file = "static/generated_music.wav"
mp3_file = "static/generated_music.mp3"

# ============================
# CHECK FILES
# ============================

if not os.path.exists(soundfont):
    raise FileNotFoundError(f"SoundFont not found:\n{soundfont}")

if not os.path.exists(midi_file):
    raise FileNotFoundError(f"MIDI file not found:\n{midi_file}")

print("Converting MIDI to WAV...")

# ============================
# MIDI -> WAV
# ============================

subprocess.run([
    "fluidsynth",
    "-ni",
    "-F", wav_file,
    "-r", "44100",
    soundfont,
    midi_file
], check=True)

print("WAV Generated Successfully!")

# ============================
# WAV -> MP3
# ============================

print("Converting WAV to MP3...")

from pydub import AudioSegment

AudioSegment.converter = r"C:\Users\OSAMA DON\Downloads\ffmpeg-8.1.2-essentials_build\ffmpeg-8.1.2-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\Users\OSAMA DON\Downloads\ffmpeg-8.1.2-essentials_build\ffmpeg-8.1.2-essentials_build\bin\ffprobe.exe"

audio = AudioSegment.from_wav(wav_file)
audio.export(mp3_file, format="mp3", bitrate="320k")

print("=" * 50)
print("MP3 Generated Successfully!")
print("Saved:", mp3_file)
print("=" * 50)