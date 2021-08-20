from pydub import AudioSegment
import os
import librosa
import numpy as np
import random
##import soundfile as sf
##from pydub.utils import mediainfo

SAMPLING_RATE = 16000
MONO = 1

Sound = "yes"

OUTPUT_FILE = "./mixedSound_"+Sound+"_"+".wav"
NOISE_FILE = "./RestaurantNoise.wav"
ORIGINAL_FILE = "./"+Sound+"_0.wav"

sound1 = AudioSegment.from_wav(NOISE_FILE)
sound2 = AudioSegment.from_wav(ORIGINAL_FILE)
tTime = random.randrange(1, 20)
tTime = tTime/10
print(tTime)
print(sound1)
##combined_sounds = sound1 + sound1 + sound1 + sound1 + sound1 # 반복 횟수 조절
##combined_sounds = combined_sounds + tTime   # dB 조절 (+ $$$), (- $$$)
combined_sounds = sound1[SAMPLING_RATE*(tTime):SAMPLING_RATE*(tTime+1)]
output = sound2.overlay(combined_sounds)
output = output.set_channels(MONO) # stereo to mono
output = output.set_frame_rate(SAMPLING_RATE) # frame_rate : 16000

output.export(OUTPUT_FILE, format="wav")

# check frame_rate
from scipy.io.wavfile import read as read_wav
import os
os.chdir('./') # path
sampling_rate, data = read_wav(OUTPUT_FILE)
print("Frame_Rate : " + str(sampling_rate))

# check channels
import wave
f1 = wave.open(OUTPUT_FILE, 'r')
print("Channels : " + str(f1.getnchannels()))


