import os

path_dir = './data/mini_speech_commands/yes'
file_list = os.listdir(path_dir)
##print(file_list)
file_string = '\n'.join(file_list)
##print(file_string)


from pydub import AudioSegment

##import soundfile as sf
##from pydub.utils import mediainfo

SAMPLING_RATE = 16000
MONO = 1

number = 46
Sound = "left"

for i in range(0, len(file_list)):
    OUTPUT_FILE = path_dir + "/" + str(file_list[i])
    NOISE_FILE = "./n" + str(number) + ".wav"
    ORIGINAL_FILE = path_dir + "/" + str(file_list[i])

    sound1 = AudioSegment.from_wav(NOISE_FILE)
    sound2 = AudioSegment.from_wav(ORIGINAL_FILE)

    combined_sounds = sound1 + sound1 + sound1 + sound1 + sound1 # 반복 횟수 조절
    combined_sounds = combined_sounds - 30   # dB 조절 (+ $$$), (- $$$)
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


