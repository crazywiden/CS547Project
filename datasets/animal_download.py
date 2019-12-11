import sys
import os


animal_name = 'blackbear'
url_filepath = animal_name+'urls.txt'
f = open(url_filepath, 'r')
lines = f.readlines()
lines = [line[:-1] for line in lines]
# os.system('wget ' + lines[1])

for i,line in enumerate(lines):
    cmd = 'wget --timeout=5 --tries=1 ' + line+' -P '+animal_name+'data'
    os.system(cmd)
    if i%100 == 0:
        print('processing ' + str(i))
f.close()