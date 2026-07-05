from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)


# ==========================
# HOME
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# TRAIN MODEL
# ==========================
@app.route("/api/train", methods=["POST"])
def train():
    try:

        subprocess.run(
            ["python", "train.py"],
            check=True
        )

        return jsonify({
            "success": True,
            "message": "Model Trained Successfully!"
        })

    except subprocess.CalledProcessError as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# ==========================
# GENERATE MUSIC
# ==========================
@app.route("/api/generate", methods=["POST"])
def generate():

    try:

        data = request.get_json()

        num_notes = str(data.get("num_notes", 100))
        genre = data.get("genre", "classical")

        subprocess.run(
            ["python", "generate.py", num_notes, genre],
            check=True
        )

        if os.path.exists("generated_music.mid"):

            return jsonify({
                "success": True,
                "message": "Music Generated Successfully!",
                "file": "generated_music.mid"
            })

        else:

            return jsonify({
                "success": False,
                "message": "generated_music.mid not found."
            })

    except subprocess.CalledProcessError as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# ==========================
# CONVERT MIDI TO MP3
# ==========================
@app.route("/api/convert", methods=["POST"])
def convert():

    try:

        result = subprocess.run(
            ["python", "midi_to_audio.py"],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )

        if result.returncode != 0:

            return jsonify({
                "success": False,
                "message": result.stderr + "\n" + result.stdout
            })

        if os.path.exists("static/generated_music.mp3"):

            return jsonify({
                "success": True,
                "message": "MP3 Generated Successfully!",
                "file": "/static/generated_music.mp3"
            })

        else:

            return jsonify({
                "success": False,
                "message": "generated_music.mp3 not found."
            })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# ==========================
# RUN FLASK
# ==========================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )