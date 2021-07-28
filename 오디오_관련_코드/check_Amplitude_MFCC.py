import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

number = 45
Sound = "left"
i = 20

OUTPUT_FILE = "./mixedSound_"+str(number)+"_"+Sound+"_"+str(i)+".wav"
NOISE_FILE = "./n"+str(number)+".wav"
ORIGINAL_FILE = "./"+Sound+"_01.wav"


### check amplitude_to_db
##y, sr = librosa.load(OUTPUT_FILE)
##D = librosa.amplitude_to_db(librosa.stft(y[:1024]), ref=np.max)
##
##plt.plot(D.flatten())
##plt.title(OUTPUT_FILE)


# check Amplitude
y, yr = librosa.load(OUTPUT_FILE)
##plt.figure()
plt.subplot(131)
librosa.display.waveplot(y, yr, alpha=0.5)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("MIXED Waveform")

x, xr = librosa.load(ORIGINAL_FILE)
##plt.figure()
plt.subplot(132)
librosa.display.waveplot(x, xr, alpha=0.5)
plt.xlabel("Time (s)")
##plt.ylabel("Amplitude")
plt.title("ORIGINAL Waveform")

z, zr = librosa.load(NOISE_FILE)
##plt.figure()
plt.subplot(133)
librosa.display.waveplot(z, zr, alpha=0.5)
plt.xlabel("Time (s)")
##plt.ylabel("Amplitude")
plt.title("NOISE Waveform")

plt.show()

# MFCC
##S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
##
##log_S = librosa.power_to_db(S, ref=np.max)
##plt.figure(figsize=(12, 4))
##librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
##plt.title('mel power spectrogram')
##plt.colorbar(format='%+02.0f dB')
##plt.tight_layout()
##plt.show()