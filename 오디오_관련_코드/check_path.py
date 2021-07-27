import os

path_dir = '../wav_file'

file_list = os.listdir(path_dir)

print(file_list)

file_string = '\n'.join(file_list)

print(file_string)

