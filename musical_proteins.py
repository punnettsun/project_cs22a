from synthesizer import Player, Synthesizer, Waveform


protein_sequence = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'

hydrophobic_aa = ['V', 'I', 'L', 'M', 'F', 'W', 'C']  # A - G major chords with sine wave
less_hydrophobic_aa = ['A', 'Y', 'H', 'T', 'S', 'P', 'G']  # A - G single notes with sine wave
part_hydrophobic_aa = ['R', 'K']  # A - G major chords with sawtooth wave
non_hydrophobic_aa = ['N', 'Q', 'D', 'E']  # A - G minor chords with sine wave

single_notes = [440.00, 493.88, 261.63, 293.66, 329.63, 349.23, 392.00]

A = [440.00, 277.18, 329.63]
B = [493.88, 311.13, 369.99]
C = [261.63, 329.63, 392.00]
D = [293.66, 369.99, 440.00]
E = [329.63, 415.30, 493.88]
F = [349.23, 440.00, 261.63]
G = [392.00, 493.88, 293.66]

major_chords = [A, B, C, D, E, F, G]

a = [440.00, 261.63, 329.63]
b = [493.88, 293.66, 369.99]
c = [261.63, 311.13, 392.00]
d = [293.66, 349.23, 440.00]
e = [329.63, 392.00, 493.88]
f = [349.23, 415.30, 261.63]
g = [392.00, 466.16, 293.66]

minor_chords = [a, b, c, d, e, f, g]

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
    print(assoc)
    return assoc

association.update(get_association(protein_sequence, hydrophobic_aa, major_chords))
association.update(get_association(protein_sequence, less_hydrophobic_aa, single_notes))
association.update(get_association(protein_sequence, part_hydrophobic_aa, major_chords, 'sawtooth'))
association.update(get_association(protein_sequence, non_hydrophobic_aa, minor_chords))

print(association)

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
        sound = synthesizer[instrument].generate_chord(note, length)
    else:
        sound = synthesizer[instrument].generate_constant_wave(note, length)

    print(aa)
    player.play_wave(sound)
