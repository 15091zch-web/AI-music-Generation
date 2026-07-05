import pickle
import random
import numpy as np
import sys

from music21 import instrument, note, chord, stream
from tensorflow.keras.models import load_model

model = load_model("music_model.keras")

with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))
n_vocab = len(pitchnames)

note_to_int = {note: num for num, note in enumerate(pitchnames)}
int_to_note = {num: note for num, note in enumerate(pitchnames)}

sequence_length = 100

# NEW: frontend support
num_notes = int(sys.argv[1]) if len(sys.argv) > 1 else 80
genre = sys.argv[2] if len(sys.argv) > 2 else "classical"

network_input = []

for i in range(len(notes) - sequence_length):
    sequence = notes[i:i + sequence_length]
    network_input.append([note_to_int[n] for n in sequence])

start = random.randint(0, len(network_input) - 1)
pattern = network_input[start]

prediction_output = []

print(f"Generating {num_notes} notes | Genre: {genre}")

for note_index in range(num_notes):

    prediction_input = np.reshape(pattern, (1, len(pattern), 1))
    prediction_input = prediction_input / float(n_vocab)

    prediction = model.predict(prediction_input, verbose=0)

    index = np.random.choice(len(prediction[0]), p=prediction[0])

    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(index)
    pattern = pattern[1:]

print("Music Generated Successfully!")

offset = 0
output_notes = []

for pattern in prediction_output:

    if '.' in pattern or pattern.isdigit():

        notes_in_chord = pattern.split('.')
        chord_notes = []

        for current_note in notes_in_chord:
            new_note = note.Note(int(current_note))
            new_note.storedInstrument = instrument.Piano()
            chord_notes.append(new_note)

        new_chord = chord.Chord(chord_notes)
        new_chord.offset = offset
        output_notes.append(new_chord)

    else:
        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()
        output_notes.append(new_note)

    offset += 0.5

midi_stream = stream.Stream(output_notes)
midi_stream.write("midi", fp="generated_music.mid")

print("====================================")
print("MIDI File Saved Successfully!")
print("====================================")