from scipy.io.wavfile import read as read_wav
import os
import wave
import contextlib


Sound_paht_dir = './datas'
Sound = os.listdir(Sound_paht_dir)
##Sound.remove('noise')
Sound.remove('test')

for k in Sound:
    print(k)
    Sound = k
    path_dir = './datas/'+k+'/'
    file_list = os.listdir(path_dir)
    print(len(file_list))
    file_string = '\n'.join(file_list)
    ##print(file_string)

    for i in range(0, len(file_list)):
        # check frame_rate
    ##    print( path_dir + str(i) )

        os.chdir('./') # path
        sampling_rate, data = read_wav(path_dir + file_list[i])
        if sampling_rate < 16000:
            print("File name : " + file_list[i] ,"Frame_Rate : " + str(sampling_rate), "Data : " + str(data))

        with contextlib.closing(wave.open(path_dir + file_list[i], 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            length = frames / float(rate)

            if length > 1:
                print("over one sec : ",file_list[i] , length)

    # check channels

##    f1 = wave.open(path_dir + str(i), 'r')
##    print("Channels : " + str(f1.getnchannels()))