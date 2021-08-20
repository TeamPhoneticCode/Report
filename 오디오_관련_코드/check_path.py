import os

path_dir = './datas/'
file_name = "yes"
file_list = os.listdir(path_dir+file_name)
print(file_list[3787])
file_string = '\n'.join(file_list)
print(file_string[-1])

##i = 0
##for filename in os.listdir(path_dir+file_name):
####    print(filename)
##    os.rename(path_dir+file_name+"/"+filename, path_dir+file_name+'/'+file_name+"_origin_"+str(i)+".wav")
##    i += 1
