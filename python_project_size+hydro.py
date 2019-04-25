#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:37:02 2019

@author: Punit Sundar
"""
from synthesizer import Player, Synthesizer, Waveform

#Lists of hydrophobicity
most_hydrophobic = ['V','I','L','M','F','W','C']
less_hydrophobic = ['A','Y','H','T','S','P','G']
part_hydrophobic = ['R','K']
not_hydrophobic = ['N','Q','D','E']

##Chords,notes,diff_inst,minor_chords & their corresponding frequencies
chords = ['A4chord','B4chord','C4chord','D4chord','E4chord','F4chord','G4chord']
chord_freq = {'A4chord':[440.00,277.18,329.63],'B4chord': [493.88,311.13,369.99],\
              'C4chord':[261.63,329.63,392.00],'D4chord': [293.66,369.99,440.00],\
              'E4chord':[329.63,415.30,493.88],'F4chord': [349.23,440.00,261.63],\
              'G4chord':[392.00,493.88,293.66]}

notes = ['A4','B4','C4','D4','E4','F4','G4']
note_freq = {'A4':440.00,'B4':493.88,'C4':261.63,'D4':293.66,'E4':\
             329.63,'F4':349.23,'G4':392.00}

diff_inst = ['C4ins','D4ins']
diff_inst_freq = {'C4ins':261.63,'D4ins':293.66}

minor_chords = ['F#minor','G#minor','Bbminor','C#minor']
minor_chord_freq = {'F#minor':[185.00,220.00,277.18],'G#minor':[207.65,246.94,311.13],\
                    'Bbminor':[233.08,277.18,349.23],'C#minor':[277.18,329.23,415.30]}

##SIZE of amino acids
small = ['A','G','S','D','C','P','N','T']
medium = ['Q','E','H','V']
large = ['R','I','L','K','M','F','W','Y']
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

def part_hydrophobic_notes(sequence):
    """Fucntion takes in sequence and converts to notes using high to low occurrence\
    association for part hydrophobic amino acids"""
    global part_hydrophobic_dict
    part_hydrophobic_dict = {}
    for amino_acids in part_hydrophobic:
        amino_count = sequence.count(amino_acids)
        part_hydrophobic_dict[amino_acids] = amino_count
    high_to_low_aa = sorted(part_hydrophobic_dict,key = part_hydrophobic_dict.get,\
                            reverse=True)[::]
    global part_hydrophobic_notes
    part_hydrophobic_notes = {}
    count = 0
    for part_occurred_amino_acid in high_to_low_aa:
        part_hydrophobic_notes[part_occurred_amino_acid] = diff_inst[count]
        count+=1
    return part_hydrophobic_notes
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
        not_hydrophobic_chords[not_occurred_amino_acid] = minor_chords[count]
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
        if amino_acids in part_hydrophobic_notes:
            transcribed_music.append(part_hydrophobic_notes[amino_acids])
        if amino_acids in not_hydrophobic_chords:
            transcribed_music.append(not_hydrophobic_chords[amino_acids])
    return transcribed_music

most = most_hydrophobic_chords(aa_sequence)
less = less_hydrophobic_notes(aa_sequence)
part = part_hydrophobic_notes(aa_sequence)
not_hy = not_hydrophobic_chords(aa_sequence)
music_sheet = transcribed_music(aa_sequence)

##For loop plays out each individual chords or notes from transcribed music

count = 0
for music in music_sheet:
    if music in chord_freq and aa_sequence[count] in small: #Chords A-G & small
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=2.0,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],0.4))
        count+=1
    elif music in chord_freq and aa_sequence[count] in medium: #Chords A-G & medium
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=2.5,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],0.4))
        count+=1
    elif music in chord_freq and aa_sequence[count] in large: #Chords A-G & large
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=3.0,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(chord_freq[music],0.4))
        count+=1
    elif music in note_freq and aa_sequence[count] in small: #Just single notes & small
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=2.0,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],0.2))
        count+=1
    elif music in note_freq and aa_sequence[count] in medium: #Just single notes & medium
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=2.5,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],0.2))
        count+=1
    elif music in note_freq and aa_sequence[count] in large: #Just single notes & large
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=3.0,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(note_freq[music],0.2))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in small:  #Different instrument & small
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.square, \
                                  osc1_volume=1.5,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(diff_inst_freq[music],0.15))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in medium:  #Different instrument & medium
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.square, \
                                  osc1_volume=2.0,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(diff_inst_freq[music],0.15))
        count+=1
    elif music in diff_inst_freq and aa_sequence[count] in large:  #Different instrument & large
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.square, \
                                  osc1_volume=2.5,use_osc2=False)
        player.play_wave(synthesizer.generate_constant_wave(diff_inst_freq[music],0.15))
        count+=1
    elif music in minor_chord_freq and aa_sequence[count] in small: #Minor chords & small
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=0.5,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(minor_chord_freq[music],0.1))
        count+=1
    elif music in minor_chord_freq and aa_sequence[count] in medium: #Minor chords & medium
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=1.0,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(minor_chord_freq[music],0.1))
        count+=1
    elif music in minor_chord_freq and aa_sequence[count] in large: #Minor chords & large
        print(aa_sequence[count])
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, \
                                  osc1_volume=1.5,use_osc2=False)
        player.play_wave(synthesizer.generate_chord(minor_chord_freq[music],0.1))
        count+=1
    else:
        print(count)
        break
    
