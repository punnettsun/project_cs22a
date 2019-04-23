#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:35:15 2019

@author: punit sundar
"""

from synthesizer import Player, Synthesizer, Waveform


chord_freq = {'A4chord': [440.00,277.18,329.63],'B4chord': [493.88,311.13,369.99],'C4chord':\
              [261.63,329.63,392.00],'D4chord': [293.66,369.99,440.00],'E4chord':\
              [329.63,415.30,493.88],'F4chord': [349.23,440.00,261.63],'G4chord':\
              [392.00,493.88,293.66]}
note_freq = {'A4':440.00,'B4':493.88,'C4':261.63,'D4':293.66,'E4':\
             329.63,'F4':349.23,'G4':392.00}
ins_notes = {'A4ins':440.00,'B4ins':493.88,'C4ins':261.63,'D4ins':293.66,'E4ins':\
             329.63,'F4ins':349.23,'G4ins':392.00}
#minor_chord_freq = {
chords = ['A4chord','B4chord','C4chord','D4chord','E4chord','F4chord','G4chord']
notes = ['A4','B4','C4','D4','E4','F4','G4']
diff_inst = ['A4ins','B4ins','C4ins','D4ins','E4ins','F4ins','G4ins']

### MVHLTPEEKS
## C4ins,A4chord,F4chord,B4chord,B4,C4,G4chord,G4chord,E4chord,F4

most_hydrophobic = ['V','I','L','M','F','W','C']
less_hydrophobic = ['A','Y','H','T','S','P','G']
part_hydrophobic = ['R','K']
not_hydrophobic = ['N','Q','D','E']

def amino_acid_occurrence(sequence):
    """Function takes in an a.a sequence & returns a dictionary\
of all occurences of each amino acid"""
    global all_counts
    all_counts = {}
    for aminos in aa_sequence:
        count = aa_sequence.count(aminos)
        all_counts[aminos] = count
    return (all_counts)

def most_frequent_to_less_frequent(all_counts):
    """Function takes in a dictionary of occurrences and orders them from\
most frequently occurring to less frequently occurring a.a"""
    global high_to_low_aa
    high_to_low_aa = sorted(all_counts,key = all_counts.get,reverse=True)[::]
    return high_to_low_aa

def most_less_part_not(high_to_low_aa):
    """Function returns 4 dictionaries with 7 amino acids at max in order of frequency"""
    count1 = 0
    global most_aa_notes
    most_aa_notes = {}
    for amino in high_to_low_aa[0:7]:
        note = chords[count1]
        most_aa_notes[amino] = note  
        count1+= 1
        
    count2 = 0
    global less_aa_notes
    less_aa_notes = {}
    for amino in high_to_low_aa[7:14]:
        note = notes[count2]
        less_aa_notes[amino] = note
        count2+= 1
        
    count3 = 0
    global part_aa_notes
    part_aa_notes = {}
    for amino in high_to_low_aa[14:21]:
        note = diff_inst[count3]
        part_aa_notes[amino] = note
        count3+= 1
        
    count4 = 0
    global not_aa_notes
    not_aa_notes = {}
    for amino in high_to_low_aa[21::]:
        note = notes[count4]  ##Different chords!
        part_aa_notes[amino] = note
        count4+= 1
    return most_aa_notes,less_aa_notes,part_aa_notes,not_aa_notes

def transcribed_music(aa_sequence):
    transcribed_music = []
    for amino_acid in aa_sequence:
        if amino_acid in most_aa_notes:  ############ADD "and in most_hydrophobic:", etc.
            transcribed_music.append(most_aa_notes[amino_acid])
        elif amino_acid in less_aa_notes:
            transcribed_music.append(less_aa_notes[amino_acid])
        elif amino_acid in part_aa_notes:
            transcribed_music.append(part_aa_notes[amino_acid])
        elif amino_acid in not_aa_notes:
            transcribed_music.append(not_aa_notes[amino_acid])
    return transcribed_music
aa_sequence = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAV\
MGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTP\
PVQAAYQKVVAGVANALAHKYH"
#A instead of G is a mutation
all_counts = amino_acid_occurrence(aa_sequence)
high_to_low_aa = most_frequent_to_less_frequent(all_counts)
most_less_part_not = most_less_part_not(high_to_low_aa)
music = transcribed_music(aa_sequence)

for music_notes in music:
    if music_notes in chord_freq:
        print('chord',chord_freq[music_notes])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine, \
                                  osc1_volume=2.0,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music_notes],0.2))
    elif music_notes in note_freq:
        print('note',note_freq[music_notes])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine, \
                                  osc1_volume=1.0,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music_notes],0.1))
    elif music_notes in ins_notes:
        print('ins',ins_notes[music_notes])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=1.0,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(ins_notes[music_notes],0.1))

    


