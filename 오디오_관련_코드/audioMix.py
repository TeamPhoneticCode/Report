from pydub import AudioSegment
import numpy
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
from pydub.utils import mediainfo
SAMPLING_RATE = 16000
MONO = 1

OUTPUT_FILE = "mixedSound_04.wav"
sound1 = AudioSegment.from_wav("./noise_04.wav")
sound2 = AudioSegment.from_wav("./example1.wav")

combined_sounds = sound1 + sound1 + sound1 + sound1 + sound1 # 반복 횟수 조절
combined_sounds = combined_sounds   # dB 조절 (+ $$$), (- $$$)
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



'''
from scipy.io import wavfile
import scipy.io
from os.path import dirname, join as pjoin

data_dir = pjoin(dirname(scipy.io.__file__), 'tests', 'data')
wav_fname = pjoin(data_dir, "mixedSound_02.wav")

samplerate, data = wavfile.read(wav_fname)
##print(f"number of channels = {data.shape[1]}")
'''

'''
import IPython as ip

info = mediainfo("./mixedSound.wav")
print(info['sample_rate'])


filename1 = "./hello.wav"
filename2 = "./Nonspeech/n3.wav"

y1, sr1 = librosa.load(filename1)
y2, sr2 = librosa.load(filename2)

#outputWav = numpy.hstack((y1,y2))

# MERGE
librosa.display.waveplot((y1+y2)/2, sr=int((sr1+sr2)/2))

# REPRODUCE
ip.display.Audio((y1+y2)/2, rate=int((sr1+sr2)/2))

#sf.write("mixSound.wav", outputWav, sr)
'''
