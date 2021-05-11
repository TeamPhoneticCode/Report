from pydub import AudioSegment


SAMPLING_RATE = 16000 # hz : 16000
MONO = 1 # mono : 1 ,,,,stereo : 2
OUTPUT_FILE = "noise11.wav" #file name

sound1 = AudioSegment.from_wav("./" + OUTPUT_FILE)
sound1 = sound1.set_channels(MONO) # stereo to mono
sound1 = sound1.set_frame_rate(SAMPLING_RATE) # frame_rate : 16000

sound1.export(OUTPUT_FILE, format="wav")