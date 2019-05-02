# music_combined_final.py
# Author: Punit Sundar & Crystal Han
# Last Updated: May 2, 2019
# Purpose: To create an association between amino acid and musical properties and use that to play out protein sequence
# Program Uses: functions, for loops, conditional statements


from synthesizer import Player, Synthesizer, Waveform
import csv


# Beta Globin protein sequence
protein_sequence = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'

hydrophobic_aa = ['V', 'I', 'L', 'M', 'F', 'W', 'C', 'A']  # G4 - A5 major chords with square wave instrument
less_hydrophobic_aa = ['Y', 'H', 'T', 'S', 'P', 'G']  # A4 - F5 single notes with sine wave instrument
non_hydrophobic_aa = ['K', 'R', 'E', 'D', 'N', 'Q']  # A4 - F5 major chords with sawtooth wave instrument

polar = ['Y', 'T', 'S', 'H', 'K', 'R', 'E', 'D', 'Q', 'N']  # Volume of 1.0
nonpolar = ['F', 'W', 'I', 'L', 'M', 'V', 'C', 'A', 'P', 'G']  # Volume of 0.5

small = ['A', 'G', 'S', 'C', 'P', 'T', 'V']  # Length of 0.1s
medium = ['N', 'D', 'E', 'Q', 'O', 'I', 'L', 'K', 'M', 'U']  # Length of 0.2s
large = ['R', 'W', 'Y', 'H', 'F']  # Length of 0.3s


# Read in frequencies of each note from CSV file
with open('./note_frequency.csv', mode='r') as file:
    reader = csv.DictReader(file)
    notes = {r['note']: float(r['frequency']) for r in reader}

# Define major chords
G4 = ['G4', 'B4', 'D5']
A4 = ['A4', 'C#5', 'E5']
B4 = ['B4', 'D#5', 'F#5']
C5 = ['C5', 'E5', 'G5']
D5 = ['D5', 'F#5', 'A5']
E5 = ['E5', 'G#5', 'B5']
F5 = ['F5', 'A5', 'C6']
G5 = ['G5', 'B5', 'D6']
A5 = ['A5', 'C#6', 'E6']

# Assign notes/chords based on hydrophobicity
hydrophobic_chords = [G4, A4, B4, C5, D5, E5, F5, G5, A5]
less_hydrophobic_notes = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5']
non_hydrophobic_chords = [A4, B4, C5, D5, E5, F5]

# Create a list of notes (starting from lowest note used) that will be printed when playing protein sequence
all_notes = list(notes.keys())
lowest_note = all_notes.index('G4')
note_range = all_notes[lowest_note:]

# Create dictionary that will map each amino acid to the various musical properties
association = {}


def get_sorted_aa(sequence, amino_acids):
    """Returns sorted list of amino acids ordered from most to least frequently occurring in the protein sequence."""
    freq = {}
    for aa in amino_acids:
        freq[aa] = sequence.count(aa)
    return sorted(freq, key=lambda x: freq[x], reverse=True)


def get_size_polarity(aa):
    """Returns whether the amino acid is polar or nonpolar as well as the volume of the note/chord based on its size."""
    if aa in small and aa in nonpolar:
        return 'nonpolar', 0.1
    if aa in small and aa in polar:
        return 'polar', 0.1
    if aa in medium and aa in nonpolar:
        return 'nonpolar', 0.2
    if aa in medium and aa in polar:
        return 'polar', 0.2
    if aa in large and aa in nonpolar:
        return 'nonpolar', 0.3
    if aa in large and aa in polar:
        return 'polar', 0.3


def get_association(sequence, amino_acids, notes, instrument):
    """Maps each amino acid to a tuple of musical properties, including note/chord, instrument, volume, and length."""
    sorted_aa = get_sorted_aa(sequence, amino_acids)
    assoc = {}
    for aa, note in zip(sorted_aa, notes):
        volume, length = get_size_polarity(aa)
        assoc[aa] = (note, instrument, volume, length)
    return assoc


def print_notes(note, aa):
    """Prints out the note/chord and amino acid being played."""
    note_string = aa + '\t'
    for n in note_range:
        if n in note:
            note_string += n
        else:
            note_string += ' '
    print(note_string)


# Generate association between amino acid and musical properties
association.update(get_association(protein_sequence, hydrophobic_aa, hydrophobic_chords, 'square'))
association.update(get_association(protein_sequence, less_hydrophobic_aa, less_hydrophobic_notes, 'sine'))
association.update(get_association(protein_sequence, non_hydrophobic_aa, non_hydrophobic_chords, 'sawtooth'))

# Create Player and Synthesizer objects to be used when playing protein sequence
player = Player()
player.open_stream()
synthesizer = {
    'polar': {
        'sine': Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False),
        'sawtooth': Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False),
        'square': Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
    },
    'nonpolar': {
        'sine': Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.5, use_osc2=False),
        'sawtooth': Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=0.5, use_osc2=False),
        'square': Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=0.5, use_osc2=False)
    },
}

# Loop through and play out each amino acid in the protein sequence
for idx, aa in enumerate(protein_sequence):
    note, instrument, volume, length = association[aa]

    length = length if idx != len(protein_sequence) - 1 else 1  # Set length of last note to be 1s

    if type(note) == list:  # Play chord
        sound = synthesizer[volume][instrument].generate_chord([notes[n] for n in note], length)
        print_notes(note, aa)
    else:  # Play single note
        sound = synthesizer[volume][instrument].generate_constant_wave(notes[note], length)
        print_notes([note], aa)

    player.play_wave(sound)
