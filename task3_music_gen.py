import os
import torch
import torch.nn as nn
import numpy as np
from music21 import converter, instrument, note, chord, stream

# Model Definition
class MusicLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=128, hidden_dim=256):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, num_layers=2, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x):
        embedded = self.embedding(x)
        out, _ = self.lstm(embedded)
        logits = self.fc(out[:, -1, :])
        return logits

def extract_notes_from_midi(midi_folder="midi_songs"):
    """Reads MIDI files and parses note/chord pitch sequences."""
    notes = []
    if not os.path.exists(midi_folder):
        os.makedirs(midi_folder)
        print(f"Created folder '{midi_folder}'. Place .mid files inside and re-run.")
        # Create a tiny fallback chord progression if folder is empty for testing
        return ["C4", "E4", "G4", "B4", "C5", "A4", "F4", "G4", "C4"] * 10

    for file in os.listdir(midi_folder):
        if file.endswith(".mid") or file.endswith(".midi"):
            midi = converter.parse(os.path.join(midi_folder, file))
            parts = instrument.partitionByInstrument(midi)
            notes_to_parse = parts.parts[0].recurse() if parts else midi.flat.notes
            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))
    return notes if notes else ["C4", "E4", "G4", "C5"] * 10

def generate_music():
    notes = extract_notes_from_midi()
    pitchnames = sorted(list(set(notes)))
    vocab_size = len(pitchnames)
    note_to_int = {note: i for i, note in enumerate(pitchnames)}
    int_to_note = {i: note for i, note in enumerate(pitchnames)}

    seq_length = 8
    inputs, targets = [], []
    for i in range(len(notes) - seq_length):
        inputs.append([note_to_int[n] for n in notes[i:i + seq_length]])
        targets.append(note_to_int[notes[i + seq_length]])

    X = torch.tensor(inputs, dtype=torch.long)
    Y = torch.tensor(targets, dtype=torch.long)

    model = MusicLSTM(vocab_size=vocab_size)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    print("Training minimal model...")
    model.train()
    for epoch in range(15):
        optimizer.zero_grad()
        output = model(X)
        loss = criterion(output, Y)
        loss.backward()
        optimizer.step()

    print("Generating music sequence...")
    model.eval()
    pattern = inputs[0]
    generated_notes = []

    for _ in range(30):
        input_seq = torch.tensor([pattern], dtype=torch.long)
        prediction = model(input_seq)
        predicted_idx = torch.argmax(prediction, dim=1).item()
        generated_notes.append(int_to_note[predicted_idx])
        pattern = pattern[1:] + [predicted_idx]

    # Convert notes to MIDI
    output_notes = []
    offset = 0.0
    for pattern in generated_notes:
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            chord_notes = [note.Note(int(n)) for n in notes_in_chord]
            new_chord = chord.Chord(chord_notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            output_notes.append(new_note)
        offset += 0.5

    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp='generated_output.mid')
    print("Saved generated audio sequence to 'generated_output.mid'")

if __name__ == "__main__":
    generate_music()