# 🎵 AI Music Generator using LSTM & Deep Learning

> An AI-powered music generation system that learns musical patterns from MIDI datasets using an LSTM (Long Short-Term Memory) neural network and generates original music in MIDI, WAV, and MP3 formats.

---

# 📖 Overview

AI Music Generator is a Deep Learning project that uses an LSTM neural network to learn musical patterns from MIDI music files. After training on a dataset, the model generates new musical note sequences, converts them into MIDI, WAV, and MP3 formats, and allows users to download the generated music through a modern Flask web application.

---

# ✨ Features

- 🎼 Train an AI model using MIDI datasets
- 🧠 LSTM-based Deep Learning model
- 🎹 Extract musical notes using Music21
- 🎵 Generate original AI music
- 💾 Save generated music as MIDI (.mid)
- 🔊 Convert MIDI to WAV
- 🎧 Convert WAV to MP3
- 📥 Download generated MP3 music
- 🌐 Modern Flask Web Interface
- 📊 Interactive AI Music Generator Dashboard
- 🎨 Responsive User Interface

---

# 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- Music21
- NumPy
- HTML5
- CSS3
- JavaScript
- FluidSynth
- FFmpeg
- Pydub

---

# 📂 Project Structure

```text
AI-Music-Generation/
│
├── dataset/
│
├── static/
│   ├── style.css
│   ├── script.js
│   ├── generated_music.wav
│   └── generated_music.mp3
│
├── templates/
│   └── index.html
│
├── preprocess.py
├── train.py
├── generate.py
├── midi_to_audio.py
├── app.py
├── requirements.txt
├── README.md
├── notes.pkl
├── music_model.keras
├── best_model.keras
└── generated_music.mid
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Music-Generation.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install FFmpeg

Download FFmpeg and add its **bin** folder to your system PATH.

### Install FluidSynth

Install FluidSynth and download a SoundFont (.sf2) file (e.g., GeneralUser GS).

---

# ▶️ Run the Project

### 1. Preprocess Dataset

```bash
python preprocess.py
```

### 2. Train the Model

```bash
python train.py
```

### 3. Launch the Website

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

Now you can:

- Train the model
- Generate AI Music
- Convert MIDI to MP3
- Download MP3

---

# 📊 Output

After successful generation, the project creates:

- 🎵 generated_music.mid
- 🔊 generated_music.wav
- 🎧 generated_music.mp3
- 🤖 music_model.keras
- 💾 best_model.keras

---

# 🚀 Future Improvements

- 🎼 Multiple instrument support
- 🎹 Genre-specific music generation
- 🎧 Built-in music player
- ☁️ Deploy on Render or Railway
- 🤖 Transformer-based music generation
- 🎵 Real-time AI music generation

---

# 👩‍💻 Author

**Zakia Chandio**

AI & Machine Learning Developer

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.