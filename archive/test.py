from synthesizer import Player, Synthesizer, Waveform
'''
aa_sequence = 'MVHLTPEE'

#MVHLTPEE into major chords depending on what amino acid occurs most often (not really #accurate right now since every a.a. Only occurs once except for E in our sample sequence)
E = 'A'
M = 'B'
V = 'C'
H = 'D'
L = 'E'
T = 'F'
P = 'G'
'''

# MVHLTPEE into chords, chords in pyaudio are in the form of frequencies
# Link to frequency chart: http://pages.mtu.edu/~suits/notefreqs.html
B = [493.88, 311.13, 369.99]  # B major consists of the notes B, D#, F# with these given freq.
C = [261.63, 329.63, 392.00]  # C major consists of C, E, G with these given frequencies
D = [293.66, 369.99, 440.00]  # D major consists of D, F#, A
E = [329.63, 415.30, 493.88]  # etc...
F = [349.23, 440.00, 261.63]
G = [392.00, 493.88, 293.66]
A = [440.00, 277.18, 329.63]

# So our major chord sequence for our amino acid sequence is: BCDEFGAA

major_chords = [B, C, D, E, F, G, A, A]  # List the major chords sequence
for letter in major_chords:  # For each major chord, play the sound of that major chord using the
    # listed frequencies from earlier^
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth,
                              osc1_volume=1.0, use_osc2=False)
    chord = letter
    player.play_wave(synthesizer.generate_chord(chord, 0.5))
