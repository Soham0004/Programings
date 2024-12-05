chord_steps = {
    'C': [0, 2, 4, 5, 7, 9, 11], 'C#': [1, 3, 5, 6, 8, 10, 0], 'D': [2, 4, 6, 7, 9, 11, 1],
    'D#': [3, 5, 7, 8, 10, 0, 2], 'E': [4, 6, 8, 9, 11, 1, 3], 'F': [5, 7, 9, 10, 0, 2, 4],
    'F#': [6, 8, 10, 11, 1, 3, 5], 'G': [7, 9, 11, 0, 2, 4, 6], 'G#': [8, 10, 0, 1, 3, 5, 7],
    'A': [9, 11, 1, 2, 4, 6, 8], 'A#': [10, 0, 2, 3, 5, 7, 9], 'B': [11, 1, 3, 4, 6, 8, 10]
}
def get_chord_notes(key, chord_type):
    base_notes = chord_steps[key]
    chord_notes = [str(base_notes[i % len(base_notes)]) for i in chord_type]
    chord_notes.sort()
    return chord_notes
def main():
    key = input("Enter the musical key (e.g., C, D, G): ").upper()
    chord_type = input("Enter the chord type (e.g., Major, Minor, Dominant seventh): ")
    chord_types = {
        'Major': [4, 7], 'Minor': [3, 7], 'Dominant seventh': [4, 7, 10],
        'Augmented fifth': [4, 8], 'Minor seventh': [3, 7, 10],
        'Minor fifth': [4, 6], 'Major seventh': [4, 7, 11],
        'Major sixth': [4, 7, 9], 'Diminished seventh': [3, 6, 10],
        'Minor sixth': [3, 7, 9]
    }
    if key in chord_steps and chord_type in chord_types:
        chord_notes = get_chord_notes(key, chord_types[chord_type])
        print(f"The notes of {key} {chord_type} chord are: {', '.join(chord_notes)}")
    else:
        print("Invalid key or chord type.")
if __name__ == "__main__":
    main()
