import pickle
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Input
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint

# ----------------------------
# Load Notes
# ----------------------------
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))
n_vocab = len(pitchnames)

print("=" * 50)
print("Total Notes :", len(notes))
print("Unique Notes:", n_vocab)
print("=" * 50)

# ----------------------------
# Convert Notes to Numbers
# ----------------------------
note_to_int = {note: number for number, note in enumerate(pitchnames)}

sequence_length = 100

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):
    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append([note_to_int[n] for n in sequence_in])
    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

print("Training Patterns:", n_patterns)

# ----------------------------
# Reshape Input
# ----------------------------
network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))
network_input = network_input / float(n_vocab)

network_output = to_categorical(network_output, num_classes=n_vocab)

# ----------------------------
# Build Model
# ----------------------------
model = Sequential()

model.add(Input(shape=(sequence_length, 1)))

model.add(LSTM(512, return_sequences=True))
model.add(Dropout(0.3))

model.add(LSTM(512))
model.add(Dropout(0.3))

model.add(Dense(256, activation="relu"))
model.add(Dense(n_vocab, activation="softmax"))

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

model.summary()

# ----------------------------
# Save Best Model
# ----------------------------
checkpoint = ModelCheckpoint(
    "best_model.keras",
    monitor="loss",
    verbose=1,
    save_best_only=True,
    mode="min"
)

# ----------------------------
# Train
# ----------------------------
print("\nTraining Started...\n")

history = model.fit(
    network_input,
    network_output,
    epochs=50,
    batch_size=64,
    callbacks=[checkpoint]
)

# ----------------------------
# Save Final Model
# ----------------------------
model.save("music_model.keras")

print("=" * 50)
print("Training Completed Successfully!")
print("Saved: music_model.keras")
print("Saved: best_model.keras")
print("=" * 50)