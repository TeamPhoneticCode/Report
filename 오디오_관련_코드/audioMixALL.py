import os
from pydub import AudioSegment
import random

##import soundfile as sf
##from pydub.utils import mediainfo

SAMPLING_RATE = 16000
MONO = 1

Sound_paht_dir = './datas'
Sound = os.listdir(Sound_paht_dir)
Sound.remove('noise')
Sound.remove('test')
for k in Sound:
    print(k)

    Original_path_dir = './speech_commands_v0.02/speech_commands_v0.02/'+k+'/'

    Output_path_dir = './datas/'

    file_list = os.listdir(Original_path_dir)
    ##print(file_list)
    file_string = '\n'.join(file_list)
    ##print(file_string)


    for i in range(0, int(len(file_list)/5)):
        ORIGINAL_FILE = Original_path_dir + str(file_list[i])
        NOISE_FILE = "./RestaurantNoise.wav"
        OUTPUT_FILE = Output_path_dir + k + '/' + k + "_random_" + str(i)+".wav"
        tTime = random.randrange(1, 20)
        tTime = tTime/10

        sound1 = AudioSegment.from_wav(NOISE_FILE)
        sound2 = AudioSegment.from_wav(ORIGINAL_FILE)

        combined_sounds = sound1[SAMPLING_RATE*(tTime):SAMPLING_RATE*(tTime+1)]
        combined_sounds = combined_sounds - tTime   # dB 조절 (+ $$$), (- $$$)
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

