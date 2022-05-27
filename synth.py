import sys
from parser2 import open_file
from scipy import signal as sg
import numpy as np
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from sys import exit

def oscilate(channel1, freq, wave, amp, seconds):
   # print("Seconds = ", seconds);
    fs = 44100
    #sin
    if (wave == 'sine'):
        buffer = amp* np.sin(2 * np.pi * np.arange(fs) * freq / fs).astype(np.float32) 
    #triangle
    if (wave =='triangle'):
        buffer = amp* np.arcsin(np.sin(2 * np.pi * np.arange(fs) * freq / fs)).astype(np.float32)
    #square
    if (wave =='square'):
        buffer = amp * sg.square(2 * np.pi * freq * np.arange(fs) / fs).astype(np.float32)
    #sawtooth
    if (wave =='sawtooth'):
        buffer = amp * sg.sawtooth(2 * np.pi * freq * np.arange(fs) / fs).astype(np.float32)
    sound = pygame.mixer.Sound(buffer)
    channel1.play(sound)
    time.sleep(seconds)
    channel1.stop()

def play_synth(tracknum, tracks_arr):
    pygame.mixer.init(size=32)

    pygame.init()


    channel1 = pygame.mixer.Channel(0)
    freqC = 16.35
    freqCs = 17.32
    freqD = 18.35
    freqDs = 19.45
    freqE = 20.60
    freqF = 21.83
    freqFs = 23.12
    freqG = 24.50
    freqGs = 25.96
    freqA = 27.50
    freqAs = 29.14
    freqB = 30.87

    octave = 4

    freq = 0
    tempo = 60
    beat = 60/int(tempo)
    for tune in tracks_arr[tracknum]['track']:

        if '1' in tune['tone']:
            octave = 0
        if '2' in tune['tone']:
            octave = 1
        if '3' in tune['tone']:
            octave = 2
        if '4' in tune['tone']:
            octave = 3
        if '5' in tune['tone']:
            octave = 4
        if '6' in tune['tone']:
            octave = 5
        if '7' in tune['tone']:
            octave = 6
        if 'c' in tune['tone']:
            freq = freqC * 2**octave
        if 'c#' in tune['tone']:
            freq = freqCs * 2**octave
        if 'd' in tune['tone']:
            freq = freqD * 2**octave
        if 'd#' in tune['tone']:
            freq = freqDs * 2**octave
        if 'e' in tune['tone']:
            freq = freqE * 2**octave
        if 'f' in tune['tone']:
            freq = freqF * 2**octave
        if 'f#' in tune['tone']:
            freq = freqFs * 2**octave
        if 'g' in tune['tone']:
            freq = freqG * 2**octave
        if  'g#' in tune['tone']:
            freq = freqGs * 2**octave
        if 'a' in tune['tone']:
            freq = freqA * 2**octave
        if 'a#' in tune['tone']:
            freq = freqAs * 2**octave
        if 'b' in tune['tone']:
            freq = freqB * 2**octave
        if 'r' in tune['tone']:
            freq = 0
                
        # print(tune['tone'])

        # print(freq)
       # print(threadname)
        oscilate(channel1, freq, tracks_arr[tracknum]['wave'], 0.1, beat * float(tune['seconds']))
def make_frequencies():
    frequencies = []
    for i in range (0, 7*12):
        frequencies.append(False)
    return frequencies

def update(dt, progressed_time, track, frequencies):
    #print(progressed_time)
    beat_num = find_beat(progressed_time, 60)
    frequencies = update_notes(beat_num, track, frequencies, progressed_time)


def find_beat(progressed_time, tempo):
    int_time = int(progressed_time)
    #print (int_time)
# def find_note(progressed_time, track):

def find_freq(tune):
    freqC = 16.35
    freqCs = 17.32
    freqD = 18.35
    freqDs = 19.45
    freqE = 20.60
    freqF = 21.83
    freqFs = 23.12
    freqG = 24.50
    freqGs = 25.96
    freqA = 27.50
    freqAs = 29.14
    freqB = 30.87

    octave = 4

    freq = 0
    if '1' in tune['tone']:
        octave = 0
    if '2' in tune['tone']:
        octave = 1
    if '3' in tune['tone']:
        octave = 2
    if '4' in tune['tone']:
        octave = 3
    if '5' in tune['tone']:
        octave = 4
    if '6' in tune['tone']:
        octave = 5
    if '7' in tune['tone']:
        octave = 6
    if 'c' in tune['tone']:
        freq = freqC * 2**octave
    if 'c#' in tune['tone']:
        freq = freqCs * 2**octave
    if 'd' in tune['tone']:
        freq = freqD * 2**octave
    if 'd#' in tune['tone']:
        freq = freqDs * 2**octave
    if 'e' in tune['tone']:
        freq = freqE * 2**octave
    if 'f' in tune['tone']:
        freq = freqF * 2**octave
    if 'f#' in tune['tone']:
        freq = freqFs * 2**octave
    if 'g' in tune['tone']:
        freq = freqG * 2**octave
    if  'g#' in tune['tone']:
        freq = freqGs * 2**octave
    if 'a' in tune['tone']:
        freq = freqA * 2**octave
    if 'a#' in tune['tone']:
        freq = freqAs * 2**octave
    if 'b' in tune['tone']:
        freq = freqB * 2**octave
    if 'r' in tune['tone']:
        freq = 0
    return freq

def update_notes(beat_num, track, frequencies, progressed_time):
    seconds = 0
    i = 0
    for tune in track['track']:
        seconds = seconds + float(tune['seconds'])
        if (seconds >= progressed_time):
            break
        i = i+1
    print (tune['tone'])
        #print (tune['tone'] + tune['seconds'])
    return frequencies

def gameloop():
    Running = True
    dt = 0
    progressed_time = 1
    clock = pygame.time.Clock()
    fps = 60
    frequencies = make_frequencies()
    tracks = open_file('Toccata.synth')
    while (Running):
        update(dt, progressed_time, tracks[5], frequencies)
        dt = clock.tick(fps)/1000.0
        progressed_time += dt



display = pygame.display.set_mode((300, 300))
# play_synth(5, file)
# #game_loop()


gameloop()
