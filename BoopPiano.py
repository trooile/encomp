import pygame
import time
import pyaudio
import analyse
import numpy
import wave
import sys
from RPi import GPIO
from array import array
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()

recorded_note = []

KEY_C = 12
KEY_D = 16
KEY_E = 18
KEY_F = 19
KEY_G = 21
KEY_H = 22
KEY_I = 23
KEY_J = 24
KEY_K = 26
KEY_L = 29
KEY_M = 31
KEY_N = 32
KEY_O = 33
KEY_P = 35
KEY_Q = 38
KEY_R = 40
KEY_S = 27
KEY_T = 28
RECORD = 37

LED = 36

freq_C = 261.6
freq_D = 293.7
freq_E = 329.6
freq_F = 349.2
freq_G = 184.9
freq_H = 220.0
freq_I = 146.8
freq_J = 130.8
freq_K = 123.4
freq_L = 116.5
freq_M = 174.6
freq_N = 277.1
freq_O = 293.6
freq_P = 311.1
freq_Q = 207.6
freq_R = 87.3
freq_S = 82.4
freq_T = 110.0
GPIO.setmode(GPIO.BOARD)

GPIO.setup(KEY_C, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_D, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_E, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_F, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_G, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_H, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_I, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_J, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_K, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_L, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_M, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_N, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_O, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_P, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_Q, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_R, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_S, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_T, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(RECORD, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(LED, GPIO.OUT)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 18
RATE = 44100
RECORD_SECONDS = ()
WAVE_OUTPUT_FILENAME = "%s filename.wav"

class ToneSound(pygame.mixer.Sound):
    def __init__(self, frequency, volume):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(pygame.mixer.get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

note_C = ToneSound(frequency = freq_C, volume = 1)
note_D = ToneSound(frequency = freq_D, volume = 1)
note_E = ToneSound(frequency = freq_E, volume = 1)
note_F = ToneSound(frequency = freq_F, volume = 1)
note_G = ToneSound(frequency = freq_G, volume = 1)
note_H = ToneSound(frequency = freq_H, volume = 1)
note_I = ToneSound(frequency = freq_I, volume = 1)
note_J = ToneSound(frequency = freq_J, volume = 1)
note_K = ToneSound(frequency = freq_K, volume = 1)
note_L = ToneSound(frequency = freq_L, volume = 1)
note_M = ToneSound(frequency = freq_M, volume = 1)
note_N = ToneSound(frequency = freq_N, volume = 1)
note_O = ToneSound(frequency = freq_O, volume = 1)
note_P = ToneSound(frequency = freq_P, volume = 1)
note_Q = ToneSound(frequency = freq_Q, volume = 1)
note_R = ToneSound(frequency = freq_R, volume = 1)
note_S = ToneSound(frequency = freq_S, volume = 1)
note_T = ToneSound(frequency = freq_T, volume = 1)

def light_off():
    GPIO.output(LED, False)

def wait_for_keydown():
    while not GPIO.input(KEY_C) and not GPIO.input(KEY_D) and not GPIO.input(KEY_E) and not GPIO.input(KEY_F) and not GPIO.input(KEY_G) and not GPIO.input(KEY_H) and not GPIO.input(KEY_I) and not GPIO.input(KEY_J) and not GPIO.input(KEY_K) and not GPIO.input(KEY_L) and not GPIO.input(KEY_M) and not GPIO.input(KEY_N) and not GPIO.input(KEY_O) and not GPIO.input(KEY_P) and not GPIO.input(KEY_Q) and not GPIO.input(KEY_R) and not GPIO.input(KEY_S) and not GPIO.input(KEY_T) and not GPIO.input(RECORD):
        time.sleep(0.01)

def wait_for_keyup(pin):
    while GPIO.input(pin):
        time.sleep(0.1)

def play_note():
    for i, v in enumerate(recorded_note):
        if v[0] is 'B':
            print(v[0], v[1])
            time.sleep(v[1])
        elif v[0] is 'C':
            print(v[0], v[1])
            note_C.play(-1)
            time.sleep(v[1])
            note_C.stop()
        elif v[0] is 'D':
            print(v[0], v[1])
            note_D.play(-1)
            time.sleep(v[1])
            note_D.stop()
        elif v[0] is 'E':
            print(v[0], v[1])
            note_E.play(-1)
            time.sleep(v[1])
            note_E.stop()
        elif v[0] is 'F':
            print(v[0], v[1])
            note_F.play(-1)
            time.sleep(v[1])
            note_F.stop()
        elif v[0] is 'G':
            print(v[0], v[1])
            note_G.play(-1)
            time.sleep(v[1])
            note_G.stop()
        elif v[0] is 'H':
            print(v[0], v[1])
            note_H.play(-1)
            time.sleep(v[1])
            note_H.stop()
        elif v[0] is 'I':
            print(v[0], v[1])
            note_I.play(-1)
            time.sleep(v[1])
            note_I.stop()
        elif v[0] is 'J':
            print(v[0], v[1])
            note_J.play(-1)
            time.sleep(v[1])
            note_J.stop()
        elif v[0] is 'K':
            print(v[0], v[1])
            note_K.play(-1)
            time.sleep(v[1])
            note_K.stop()
        elif v[0] is 'L':
            print(v[0], v[1])
            note_L.play(-1)
            time.sleep(v[1])
            note_L.stop()
        elif v[0] is 'M':
            print(v[0], v[1])
            note_M.play(-1)
            time.sleep(v[1])
            note_M.stop()
        elif v[0] is 'N':
            print(v[0], v[1])
            note_N.play(-1)
            time.sleep(v[1])
            note_N.stop()
        elif v[0] is 'O':
            print(v[0], v[1])
            note_O.play(-1)
            time.sleep(v[1])
            note_O.stop()
        elif v[0] is 'P':
            print(v[0], v[1])
            note_P.play(-1)
            time.sleep(v[1])
            note_P.stop()
        elif v[0] is 'Q':
            print(v[0], v[1])
            note_Q.play(-1)
            time.sleep(v[1])
            note_Q.stop()
        elif v[0] is 'R':
            print(v[0], v[1])
            note_R.play(-1)
            time.sleep(v[1])
            note_R.stop()
        elif v[0] is 'S':
            print(v[0], v[1])
            note_S.play(-1)
            time.sleep(v[1])
            note_S.stop()
        elif v[0] is 'T':
            print(v[0], v[1])
            note_T.play(-1)
            time.sleep(v[1])
            note_T.stop()    
            
record_flag = True

pyaudio = pyaudio.PyAudio()

frames = []

while True:
    start_time = time.time()
    wait_for_keydown()
    diff_time = time.time() - start_time
    if record_flag:
        recorded_note.append(('B', diff_time))
    if GPIO.input(KEY_C):
        start_time = time.time()
        note_C.play(-1)
        wait_for_keyup(KEY_C)
        note_C.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('C', diff_time))
    elif GPIO.input(KEY_D):
        start_time = time.time()
        note_D.play(-1)
        wait_for_keyup(KEY_D)
        note_D.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('D', diff_time))
    elif GPIO.input(KEY_E):
        start_time = time.time()
        note_E.play(-1)
        wait_for_keyup(KEY_E)
        note_E.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('E', diff_time))
    elif GPIO.input(KEY_F):
        start_time = time.time()
        note_F.play(-1)
        wait_for_keyup(KEY_F)
        note_F.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('F', diff_time))
    elif GPIO.input(KEY_G):
        start_time = time.time()
        note_G.play(-1)
        wait_for_keyup(KEY_G)
        note_G.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('G', diff_time))
    elif GPIO.input(KEY_H):
        start_time = time.time()
        note_H.play(-1)
        wait_for_keyup(KEY_H)
        note_H.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('H', diff_time))
     elif GPIO.input(KEY_I):
        start_time = time.time()
        note_I.play(-1)
        wait_for_keyup(KEY_I)
        note_I.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('I', diff_time))
     elif GPIO.input(KEY_J):
        start_time = time.time()
        note_J.play(-1)
        wait_for_keyup(KEY_J)
        note_J.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('J', diff_time))
     elif GPIO.input(KEY_K):
        start_time = time.time()
        note_K.play(-1)
        wait_for_keyup(KEY_K)
        note_K.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('K', diff_time))
     elif GPIO.input(KEY_L):
        start_time = time.time()
        note_L.play(-1)
        wait_for_keyup(KEY_L)
        note_L.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('L', diff_time))
     elif GPIO.input(KEY_M):
        start_time = time.time()
        note_M.play(-1)
        wait_for_keyup(KEY_M)
        note_M.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('M', diff_time))
     elif GPIO.input(KEY_N):
        start_time = time.time()
        note_N.play(-1)
        wait_for_keyup(KEY_N)
        note_N.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('N', diff_time))
     elif GPIO.input(KEY_O):
        start_time = time.time()
        note_O.play(-1)
        wait_for_keyup(KEY_O)
        note_O.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('O', diff_time))
     elif GPIO.input(KEY_P):
        start_time = time.time()
        note_P.play(-1)
        wait_for_keyup(KEY_P)
        note_P.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('P', diff_time))
     elif GPIO.input(KEY_Q):
        start_time = time.time()
        note_Q.play(-1)
        wait_for_keyup(KEY_Q)
        note_Q.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('Q', diff_time))
     elif GPIO.input(KEY_R):
        start_time = time.time()
        note_R.play(-1)
        wait_for_keyup(KEY_R)
        note_R.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('R', diff_time))
     elif GPIO.input(KEY_S):
        start_time = time.time()
        note_S.play(-1)
        wait_for_keyup(KEY_S)
        note_S.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('S', diff_time))
     elif GPIO.input(KEY_T):
        start_time = time.time()
        note_T.play(-1)
        wait_for_keyup(KEY_T)
        note_T.stop()
        diff_time = time.time() - start_time
        if record_flag:
            recorded_note.append(('T', diff_time))
    elif GPIO.input(RECORD):
        if record_flag == False:
            recorded_note = []
            stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
            print('Recording started!')
        else:
            print('Recording stopped!')
        record_flag = not record_flag
        stream.stop_stream()
          stream.close()
          p.terminate()
          RECORD1 = wave.open(WAVE_OUTPUT_FILENAME, '1')
          RECORD1.setnchannels(CHANNELS)
          RECORD1.setsampwidth(p.get_sample_size(FORMAT))
          RECORD1.setframerate(RATE)
          RECORD1.writeframes(B''.join(frames))
          RECORD1.close()
        time.sleep(.5)
        GPIO.output(LED, record_flag)
        light_off()

