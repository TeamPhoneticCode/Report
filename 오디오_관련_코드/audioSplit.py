import librosa
import numpy as np
import soundfile as sf
import os
import matplotlib.pyplot as plt

sr = 16000
mono = 1

TestFile = './RestaurantNoise.wav'

file_dir, file_id = os.path.split(TestFile)

y, sr = librosa.load(TestFile, sr = sr)
time = np.linspace(0, len(y)/sr, len(y))
fig, ax1 = plt.subplots() # plot
ax1.plot(time, y, color = 'b', label='speech waveform')
ax1.set_ylabel("Amplitude") # y 축
ax1.set_xlabel("Time [s]") # x 축
plt.title(file_id) # 제목
plt.savefig(file_id+'.png')
plt.show()

librosa.output.write_wav('cut_file.wav', y1/2, sr)