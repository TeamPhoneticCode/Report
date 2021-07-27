OUTPUT_FILE = "example1.wav" #file name

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