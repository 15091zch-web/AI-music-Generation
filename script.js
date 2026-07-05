const API_URL = "/api";

function updateNoteValue(value) {
    document.getElementById("noteValue").innerText = value;
}

function showStatus(id, msg, type = "processing") {
    const el = document.getElementById(id);
    el.innerHTML = msg;
    el.className = "status-message " + type;
}

function addLog(msg) {
    const logs = document.getElementById("logs");

    if (!logs) return;

    const time = new Date().toLocaleTimeString();

    logs.innerHTML =
        `<div>[${time}] ${msg}</div>`;
}

// ==============================
// TRAIN
// ==============================

function trainModel() {

    const dataset = document.getElementById("datasetPath").value;

    showStatus(
        "trainStatus",
        "⏳ Training...",
        "processing"
    );

    addLog("Training Started");

    fetch(API_URL + "/train", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            dataset_path: dataset
        })

    })

    .then(res => res.json())

    .then(data => {

        if (data.success) {

            showStatus(
                "trainStatus",
                "✅ " + data.message,
                "success"
            );

            addLog("Training Completed");

        }

        else {

            showStatus(
                "trainStatus",
                "❌ " + data.message,
                "error"
            );

        }

    });

}

// ==============================
// GENERATE
// ==============================

function generateMusic() {

    const notes =
        document.getElementById("numNotes").value;

    const genre =
        document.getElementById("genre").value;

    showStatus(
        "generateStatus",
        "⏳ Generating Music...",
        "processing"
    );

    addLog("Generating Music...");

    fetch(API_URL + "/generate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            num_notes: notes,
            genre: genre

        })

    })

    .then(res => res.json())

    .then(data => {

        if (data.success) {

            showStatus(
                "generateStatus",
                "✅ Music Generated Successfully!",
                "success"
            );

            addLog("Music Generated");

            document.getElementById("midiFile").value =
                data.file;

        }

        else {

            showStatus(
                "generateStatus",
                "❌ " + data.message,
                "error"
            );

        }

    });

}

// ==============================
// CONVERT
// ==============================

function convertMIDI() {

    showStatus(
        "convertStatus",
        "⏳ Creating MP3...",
        "processing"
    );

    addLog("Converting...");

    fetch(API_URL + "/convert", {

        method: "POST"

    })

    .then(res => res.json())

    .then(data => {

        if (data.success) {

            showStatus(
                "convertStatus",
                "✅ MP3 Ready!",
                "success"
            );

            addLog("MP3 Created");

        }

        else {

            showStatus(
                "convertStatus",
                "❌ " + data.message,
                "error"
            );

        }

    });

}

// ==============================
// DOWNLOAD
// ==============================

function downloadMP3() {

    window.open(
        "/static/generated_music.mp3",
        "_blank"
    );

}