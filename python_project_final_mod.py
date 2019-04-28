#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:11:13 2019

@author: vsundaramurthy
"""

from synthesizer import Player, Synthesizer, Waveform

##Ascending chords: A4,B4,C5,D5,E5,F5,G5
#Lists of hydrophobicity
most_hydrophobic = ['V','I','L','M','F','W','C','A','M']
less_hydrophobic = ['Y','H','T','S','P','G']
not_hydrophobic = ['K','R','E','D','N','Q']


##Chords,notes,diff_inst,minor_chords & their corresponding frequencies
chords = ['G4chord','A4chord','B4chord','C5chord','D5chord','E5chord','F5chord','G5chord','A5chord']

chord_freq = {'G4chord': [392.00,493.88,293.66],'A4chord':[440.00,554.37,659.25],\
              'B4chord': [493.88,622.25,739.99],'C5chord':[523.25,659.25,783.99],\
              'D5chord': [587.33,739.99,880.00],'E5chord':[659.25,830.61,987.77],\
              'F5chord': [698.46,880.00,1046.50],'G5chord':[783.99,987.77,1174.66],\
              'A5chord': [880.00,1108.73,1318.51]}

notes = ['A4','B4','C5','D5','E5','F5','G5']
'''
note_freq = {'A4':440.00,'B4':493.88,'C5':261.63,'D5':293.66,'E5':\
             329.63,'F5':349.23,'G5':392.00}
'''
note_freq = {'A4':440.00,'B4':493.88,'C5':523.25,'D5':587.33,'E5':\
             659.25,'F5':698.46}

diff_inst = ['A4ins','B4ins','C5ins','D5ins','E5ins','F5ins']
#diff_inst_freq = {'C5ins':261.63,'D5ins':293.66}

diff_inst_freq = {'A4ins':[440.00,554.37,659.25],\
              'B4ins': [493.88,622.25,739.99],'C5ins':[523.25,659.25,783.99],\
              'D5ins': [587.33,739.99,880.00],'E5ins':[659.25,830.61,987.77],\
              'F5ins': [698.46,880.00,1046.50]}


##old SIZE of amino acids
#small = ['A','G','S','D','C','P','N','T']
#medium = ['Q','E','H','V']
#large = ['R','I','L','K','M','F','W','Y']

small = ['A','G','S','C','P','T','V']
medium = ['N','D','E','Q','O','I','L','K','M','U']
large = ['R','W','Y','H','F']

##Nonpolar/Polar
nonpolar = ['F','W','I','L','M','V','C','A','P','G']
polar = ['Y','T','S','H','K','R','E','D','Q','N']
#Amino acid sequence

aa_sequence = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAV\
MGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTP\
PVQAAYQKVVAGVANALAHKYH"


#Functions to order amino acid associations from greatest to least hydrophobicity
def most_hydrophobic_chords(sequence):
    """Fucntion takes in sequence and converts to chords using high to low occurrence\
    association for most hydrophobic amino acids"""
    global most_hydrophobic_dict
    most_hydrophobic_dict = {}
    for amino_acids in most_hydrophobic:
        amino_count = sequence.count(amino_acids)
        most_hydrophobic_dict[amino_acids] = amino_count
    high_to_low_aa = sorted(most_hydrophobic_dict,key = most_hydrophobic_dict.get,\
                            reverse=True)[::]
    global hydrophobic_chords
    hydrophobic_chords = {}
    count = 0
    for most_occurred_amino_acid in high_to_low_aa:
        hydrophobic_chords[most_occurred_amino_acid] = chords[count]
        count+=1
    return hydrophobic_chords

def less_hydrophobic_notes(sequence):
    """Fucntion takes in sequence and converts to notes using high to low occurrence\
    association for less hydrophobic amino acids"""
    global less_hydrophobic_dict
    less_hydrophobic_dict = {}
    for amino_acids in less_hydrophobic:
        amino_count = sequence.count(amino_acids)
        less_hydrophobic_dict[amino_acids] = amino_count
    high_to_low_aa = sorted(less_hydrophobic_dict,key = less_hydrophobic_dict.get,\
                            reverse=True)[::]
    global less_hydrophobic_notes
    less_hydrophobic_notes = {}
    count = 0
    for less_occurred_amino_acid in high_to_low_aa:
        less_hydrophobic_notes[less_occurred_amino_acid] = notes[count]
        count+=1
    return less_hydrophobic_notes

def not_hydrophobic_chords(sequence):
    """Fucntion takes in sequence and converts to notes using high to low occurrence\
    association for not hydrophobic amino acids"""
    global not_hydrophobic_dict
    not_hydrophobic_dict = {}
    for amino_acids in not_hydrophobic:
        amino_count = sequence.count(amino_acids)
        not_hydrophobic_dict[amino_acids] = amino_count
    high_to_low_aa = sorted(not_hydrophobic_dict,key = not_hydrophobic_dict.get,\
                            reverse=True)[::]
    global not_hydrophobic_chords
    not_hydrophobic_chords = {}
    count = 0
    for not_occurred_amino_acid in high_to_low_aa:
        not_hydrophobic_chords[not_occurred_amino_acid] = diff_inst[count]
        count+=1
    return not_hydrophobic_chords

def transcribed_music(sequence):
    """Function takes in sequence and converts individual amino acids into either \
chords,notes,diff_inst,or minor_chords"""
    transcribed_music = []
    for amino_acids in sequence:
        if amino_acids in hydrophobic_chords:
            transcribed_music.append(hydrophobic_chords[amino_acids])
        if amino_acids in less_hydrophobic_notes:
            transcribed_music.append(less_hydrophobic_notes[amino_acids])
        if amino_acids in not_hydrophobic_chords:
            transcribed_music.append(not_hydrophobic_chords[amino_acids])
    return transcribed_music

most = most_hydrophobic_chords(aa_sequence)
less = less_hydrophobic_notes(aa_sequence)
not_hy = not_hydrophobic_chords(aa_sequence)
music_sheet = transcribed_music(aa_sequence)

##Set base values for instrument change, polar/nonpolar, size
player = Player()
player.open_stream()
instrument1 = osc1_waveform=Waveform.sine #main instrument
instrument2 = osc1_waveform=Waveform.sawtooth #diff instrument
volume1 = osc1_volume=0.5  #nonpolar
volume2 = osc1_volume=1.0  #polar
length = [0.1,0.2,0.3]  #based on size from smallest to largest

##For loop plays out each individual chords or notes from transcribed music
count = 0
for music in music_sheet:
    if music in chord_freq and aa_sequence[count] in small and aa_sequence[count] in nonpolar: #Chords A-G & small
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],length[0]))
        count+=1
    elif music in chord_freq and aa_sequence[count] in small and aa_sequence[count] in polar: #Chords A-G & small
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],length[0]))
        count+=1
    elif music in chord_freq and aa_sequence[count] in medium and aa_sequence[count] in nonpolar: #Chords A-G & medium
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],length[1]))
        count+=1
    elif music in chord_freq and aa_sequence[count] in medium and aa_sequence[count] in polar: #Chords A-G & medium
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],length[1]))
        count+=1
    elif music in chord_freq and aa_sequence[count] in large and aa_sequence[count] in nonpolar: #Chords A-G & large
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],length[2]))
        count+=1
    elif music in chord_freq and aa_sequence[count] in large and aa_sequence[count] in polar: #Chords A-G & large
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],length[2]))
        count+=1
    elif music in note_freq and aa_sequence[count] in small and aa_sequence[count] in nonpolar: #Just single notes & small
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],length[0]))
        count+=1
    elif music in note_freq and aa_sequence[count] in small and aa_sequence[count] in polar: #Just single notes & small
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],length[0]))
        count+=1
    elif music in note_freq and aa_sequence[count] in medium and aa_sequence[count] in nonpolar: #Just single notes & medium
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],length[1]))
        count+=1
    elif music in note_freq and aa_sequence[count] in medium and aa_sequence[count] in polar: #Just single notes & medium
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],length[1]))
        count+=1
    elif music in note_freq and aa_sequence[count] in large and aa_sequence[count] in nonpolar: #Just single notes & large
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],length[2]))
        count+=1
    elif music in note_freq and aa_sequence[count] in large and aa_sequence[count] in polar: #Just single notes & large
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument1, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],length[2]))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in small and aa_sequence[count] in nonpolar:  #Different instrument & small
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument2, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(diff_inst_freq[music],length[0]))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in small and aa_sequence[count] in polar:  #Different instrument & small
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument2, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(diff_inst_freq[music],length[0]))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in medium and aa_sequence[count] in nonpolar:  #Different instrument & medium
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument2, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(diff_inst_freq[music],length[1]))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in medium and aa_sequence[count] in polar:  #Different instrument & medium
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument2, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(diff_inst_freq[music],length[1]))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in large and aa_sequence[count] in nonpolar:  #Different instrument & large
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument2, \
                                  volume1,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(diff_inst_freq[music],length[2]))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in large and aa_sequence[count] in polar:  #Different instrument & large
        print(aa_sequence[count])
        synthesizer = Synthesizer(instrument2, \
                                  volume2,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(diff_inst_freq[music],length[2]))
        count+=1
    else:
        print(count)
        break
    
