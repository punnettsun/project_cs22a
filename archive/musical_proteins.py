from synthesizer import Player, Synthesizer, Waveform
import csv


protein_sequence = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'

hydrophobic_aa = ['V', 'I', 'L', 'M', 'F', 'W', 'C']  # A - G major chords with sine wave
less_hydrophobic_aa = ['A', 'Y', 'H', 'T', 'S', 'P', 'G']  # A - G single notes with sine wave
part_hydrophobic_aa = ['R', 'K']  # A - G major chords with sawtooth wave
non_hydrophobic_aa = ['N', 'Q', 'D', 'E']  # A - G minor chords with sine wave

small = ['A', 'G', 'S', 'D', 'C', 'P', 'N', 'T']
medium = ['Q', 'E', 'H', 'V']
large = ['R', 'I', 'L', 'K', 'M', 'F', 'W', 'Y']

with open('./note_frequency.csv', mode='r') as file:
    reader = csv.DictReader(file)
    notes = {r['note']: float(r['frequency']) for r in reader}


# A4 through D#6
note_range = list(notes.keys())[57:76]
# print(note_range)

single_notes = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']

A = ['A4', 'C#5', 'E5']
B = ['B4', 'D#5', 'F#5']
C = ['C5', 'E5', 'G5']
D = ['D5', 'F#5', 'A5']
E = ['E5', 'G#5', 'B5']
F = ['F5', 'A5', 'C6']
G = ['G5', 'B5', 'D6']

major_chords = [A, B, C, D, E, F, G]
extra_chords = [C, D]

f_sharp = ['F#5', 'A5', 'C#6']
g_sharp = ['G#5', 'B5', 'D#6']
a_sharp = ['A#4', 'C#5', 'F5']
c_sharp = ['C#5', 'E5', 'G#5']

minor_chords = [f_sharp, g_sharp, a_sharp, c_sharp]

association = {}


def get_sorted_aa(sequence, amino_acids):
    freq = {}
    for aa in amino_acids:
        freq[aa] = sequence.count(aa)
    # print(freq)
    return sorted(freq, key=lambda x: freq[x], reverse=True)


def get_association(sequence, amino_acids, notes, instrument='sine'):
    sorted_aa = get_sorted_aa(sequence, amino_acids)
    assoc = {}
    for aa, note in zip(sorted_aa, notes):
        assoc[aa] = (note, instrument)
    # print(assoc)
    return assoc


def print_notes(note):
    note_string = ''
    for n in note_range:
        if n in note:
            note_string += n
        else:
            note_string += ' '
    print(note_string)


association.update(get_association(protein_sequence, hydrophobic_aa, major_chords))
association.update(get_association(protein_sequence, less_hydrophobic_aa, single_notes))
association.update(get_association(protein_sequence, part_hydrophobic_aa, extra_chords, 'sawtooth'))
association.update(get_association(protein_sequence, non_hydrophobic_aa, minor_chords))

# print(association)

player = Player()
player.open_stream()
synthesizer = {
    'sine': Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False),
    'sawtooth': Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
}

for idx, aa in enumerate(protein_sequence):
    note, instrument = association[aa]

    length = 0.2 if idx != len(protein_sequence) - 1 else 1

    if type(note) == list:
        sound = synthesizer[instrument].generate_chord([notes[n] for n in note], length)
        print_notes(note)
    else:
        sound = synthesizer[instrument].generate_constant_wave(notes[note], length)
        print_notes([note])

    player.play_wave(sound)
