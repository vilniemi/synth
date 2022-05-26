
import pygame
from scipy import signal as sg
import numpy as np
import time

def oscilate(channel1, freq, amp, seconds):
    fs = 44100
    #sin
    buffer = amp* np.sin(2 * np.pi * np.arange(fs) * freq / fs).astype(np.float32) 
    #triangle
   # buffer = amp* np.arcsin(np.sin(2 * np.pi * np.arange(fs) * freq / fs)).astype(np.float32)
    #square
    #buffer = amp * sg.square(2 * np.pi * freq * np.arange(fs) / fs).astype(np.float32)
    #sawtooth
    #buffer = amp * sg.sawtooth(2 * np.pi * freq * np.arange(fs) / fs).astype(np.float32)
    duration = 2
    #buffer = (np.modf(np.arange(fs*duration)*freq/fs)[0]*2.0-1.0).astype(np.float32)
    sound = pygame.mixer.Sound(buffer)
    #channel1.play(sound, loops = -1)
    channel1.play(sound)
    time.sleep(seconds)
    channel1.fadeout(1)
    #channel1.stop()
    #pygame.time.wait(int(sound.get_length() * 1))


pygame.mixer.init(size=32)

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((300, 300))
channel1 = pygame.mixer.Channel(0)
freq = 440
while(True):
    freq = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                freq = 110
            elif( event.key == pygame.K_x):
                freq = 210
            elif(event.key ==  pygame.K_c):
                freq = 310
            oscilate(channel1, freq, 1, 2)

        if event.type == pygame.KEYUP:
            #channel1.fadeout(2000)
            channel1.stop()
            print ('key up')
                
                #oscilate(freq)
