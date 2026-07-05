from music21 import converter, instrument, note, chord
import glob
import pickle

# List to store all notes
notes = []

# Read all MIDI files from dataset folder
for file in glob.glob("dataset/*.mid"):

    print("Reading:", file)

    midi = converter.parse(file)

    notes_to_parse = None

    try:
        parts = instrument.partitionByInstrument(midi)

        if parts:
            notes_to_parse = parts.parts[0].recurse()
        else:
            notes_to_parse = midi.flat.notes

    except:
        notes_to_parse = midi.flat.notes

    # Extract notes and chords
    for element in notes_to_parse:

        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

# Save notes into a file
with open("notes.pkl", "wb") as filepath:
    pickle.du
    mp(notes, filepath)

print("===================================")
print("Preprocessing Completed Successfully!")
print("Total Notes:", len(notes))
print("notes.pkl file created.")
print("===================================")