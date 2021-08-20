from pydub import AudioSegment
import os
import librosa
print(librosa.__version__)
import numpy as np

SAMPLING_RATE = 16000 # hz : 16000
MONO = 1 # mono : 1 ,,,,stereo : 2
OUTPUT_FILE = 'RestaurantNoise.wav' #file name
Sec = 3

path_dir = './'
file_list = os.listdir(path_dir)
for i in file_list:
    if i == OUTPUT_FILE:
        break
print(i)

sound1 = AudioSegment.from_wav(path_dir + OUTPUT_FILE)
##sound1 = AudioSegment.from_mp3("./" + OUTPUT_FILE)
sound1 = sound1.set_channels(MONO) # stereo to mono
sound1 = sound1.set_frame_rate(SAMPLING_RATE) # frame_rate : 16000

sound1.export(OUTPUT_FILE, format="wav")

y, sr = librosa.load(path_dir + OUTPUT_FILE)
print(y, sr)
ny = y[:sr*Sec]
librosa.output.write_wav("cut_" + OUTPUT_FILE, ny, sr)