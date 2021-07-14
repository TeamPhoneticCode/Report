import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

number = 45

OUTPUT_FILE = "./mixedSound_"+str(number)+".wav"

# check amplitude_to_db
y, sr = librosa.load(OUTPUT_FILE)
D = librosa.amplitude_to_db(librosa.stft(y[:1024]), ref=np.max)

plt.plot(D.flatten())
plt.title(OUTPUT_FILE)
plt.show()

# MFCC
S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

log_S = librosa.power_to_db(S, ref=np.max)
plt.figure(figsize=(12, 4))
librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
plt.title('mel power spectrogram')
plt.colorbar(format='%+02.0f dB')
plt.tight_layout()
plt.show()