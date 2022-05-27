import sys
from parser2 import open_file
from scipy import signal as sg
import numpy as np
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from sys import exit 
from multiprocessing import Process
import re

def oscilate(instruments, amp, dt):
    fs = 44100
    for instrument in instruments:
        wave = instrument['wave']
        freq = instrument['freq']
        channel = instrument['channel']
        if (wave == 'sine'):
            buffer = amp* np.sin(2 * np.pi * np.arange(fs) * freq / fs).astype(np.float32) 
        if (wave =='triangle'):
            buffer = amp* np.arcsin(np.sin(2 * np.pi * np.arange(fs) * freq / fs)).astype(np.float32)
        if (wave =='square'):
            buffer = amp * sg.square(2 * np.pi * freq * np.arange(fs) / fs).astype(np.float32)
        if (wave =='saw'):
            buffer = amp * sg.sawtooth(2 * np.pi * freq * np.arange(fs) / fs).astype(np.float32)

        sound = pygame.mixer.Sound(buffer)
        if (instrument['just_started'] == True and freq != 0):
            instrument['just_started'] = False
            channel.play(sound, maxtime=int(instrument['seconds']*1000))

def find_beat(progressed_time, tempo):
    int_time = int(progressed_time)
    return int_time

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
    if ('c' in tune['tone'] and '#' in tune['tone']) or ('d' in tune['tone'] and 'b' in tune['tone']):
        freq = freqCs * 2**octave
    elif 'c' in tune['tone']:
        freq = freqC * 2**octave
    elif ('d' in tune['tone'] and '#' in tune['tone']) or ('e' in tune['tone'] and 'b' in tune['tone']):
        freq = freqDs * 2**octave
    elif 'd' in tune['tone']:
        freq = freqD * 2**octave
    elif 'e' in tune['tone']:
        freq = freqE * 2**octave
    elif ('f' in tune['tone'] and '#' in tune['tone']) or ('g' in tune['tone'] and 'b' in tune['tone']):
        freq = freqFs * 2**octave
    elif 'f' in tune['tone']:
        freq = freqF * 2**octave
    elif ('g' in tune['tone'] and '#' in tune['tone']) or ('a' in tune['tone'] and 'b' in tune['tone']):
        freq = freqGs * 2**octave
    elif 'g' in tune['tone']:
        freq = freqG * 2**octave
    elif ('a' in tune['tone'] and '#' in tune['tone']) or (re.search("b\d*b", tune['tone'])):
        freq = freqAs * 2**octave
    elif 'a' in tune['tone']:
        freq = freqA * 2**octave
    elif 'b' in tune['tone']:
        freq = freqB * 2**octave
    elif 'r' in tune['tone']:
        freq = 0
    return freq

def update_instrument(instrument, progressed_time, beat):
    seconds = 0
    track = instrument['track']
    i = 0
    for tune in track['track']:
        seconds = seconds + 60/int(beat)*float(tune['seconds'])
        if (seconds >= progressed_time):
            break
        i = i+1
    instrument['freq'] = find_freq(tune)
    if i != instrument['lastfreq']:
        instrument['lastfreq'] = i
        instrument['just_started'] = True
        instrument['seconds'] = float(tune['seconds'])
    return instrument

def check_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
def find_length(tracks, beat):
    longest_length = 0
    seconds = 0
    for track in tracks:
        for tune in track['track']:
            seconds = seconds + 60/int(beat)*float(tune['seconds'])
        if seconds > longest_length:
            longest_length = seconds
        seconds = 0
    return (longest_length)


def gameloop(filename):
    pygame.mixer.init(size=32)
    pygame.init()
    pygame.display.set_caption('minisynth')
    #pygame.display.set_icon(Icon_name)
    Running = True
    dt = 0
    progressed_time = 1
    clock = pygame.time.Clock()
    fps = 60
    tracksparser = open_file(filename)
    tracks = tracksparser[0]
    tempo = tracksparser[1]
    pygame.mixer.set_num_channels(len(tracks))
    instruments = []
    i = 0
    length = find_length(tracks, tempo)
    for track in tracks:
        instrument = {}
        instrument['freq'] = 0
        instrument['playing'] = False
        instrument['time'] = 0
        instrument['wave'] = track['wave']
        instrument['track'] = track
        instrument['seconds'] = 0 
        instrument['lastfreq'] = -1
        instrument['just_started'] = False
        instrument['channel'] = pygame.mixer.Channel(i)
        instruments.append(instrument)
        i+=1
    last_beat = -1

    while (Running):
            for instrument in instruments:
                update_instrument(instrument, progressed_time, tempo)
            current_beat = find_beat(progressed_time, tempo)
            if (current_beat != last_beat):
                print("\r", end="")
                i = 1
                num_bar = 50
                print("time: ", int(progressed_time), "/", int(length), end="")
                #print("["+str(current_beat)+"]")
                last_beat = current_beat
            oscilate(instruments,  0.1, dt)
            dt = clock.tick(fps)/1000.0
            check_keys()
            progressed_time += dt
            if progressed_time > length:
                exit()

display = pygame.display.set_mode((300, 300))
if (len(sys.argv) < 2):
    print ("give filename")
    exit(0)

filename = sys.argv[1]
gameloop(filename)

# while(True):
#     freq = 0
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 freq = freqC * 2**octave;
#             elif( event.key == pygame.K_w):
#                 freq = freqCs * 2**octave;
#             elif( event.key == pygame.K_s):
#                 freq = freqD * 2**octave;
#             elif( event.key == pygame.K_e):
#                 freq = freqDs * 2**octave;
#             elif(event.key ==  pygame.K_d):
#                 freq = freqE * 2**octave;
#             elif(event.key ==  pygame.K_f):
#                 freq = freqF * 2**octave;
#             elif( event.key == pygame.K_t):
#                 freq = freqFs * 2**octave;
#             elif(event.key ==  pygame.K_g):
#                 freq = freqG * 2**octave;
#             elif( event.key == pygame.K_y):
#                 freq = freqGs * 2**octave;
#             elif(event.key ==  pygame.K_h):
#                 freq = freqA * 2**octave;
#             elif( event.key == pygame.K_u):
#                 freq = freqAs * 2**octave;
#             elif(event.key ==  pygame.K_j):
#                 freq = freqB * 2**octave;
#             elif(event.key == pygame.K_UP):
#                 octave += 1;
#             elif(event.key == pygame.K_DOWN):
#                 octave -= 1;
#             oscilate(channel1, freq, 1, 2)

#         if event.type == pygame.KEYUP:
#             channel1.stop()
#             print ('key up')
#     clock.tick(50)