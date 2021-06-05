'''
This program is based on the command below:
iconv -c -f GB2312 -t UTF-8 [你要看的文件] >> [新文件的名称]
'''

import os
from pathlib import Path
import subprocess

print('txt decoder running')
mode = input('single file? (y/n) \n')
#new_file = str(input('name of the new file: \n')) + 'txt'

if mode == 'y':
    file = str(input('name of the file to decode: \n')) + '.txt'
    #decoding a single file
    decoded = file[:-4] + ' decoded'
    
    os.system('iconv -c -f GB2312 -t UTF-8 %s >> %s' % (file, file[:-4]))
    os.makedirs(decoded)
    os.system("mv %s '%s'" % (file[:-4],decoded))
    
else:
    folder = str(input('name of the folder that contains all the file for decoding: \n'))
    folder_path = os.path.abspath(folder)
    os.chdir(folder_path)
    new_dir = 'the decoded files'

    file_list = [elem for elem in os.listdir(folder_path) if ".txt" in elem]
    print("file list:", file_list)

    os.makedirs(new_dir)
    for elem in file_list:
        new_name = str(elem)[:-4]
        print(elem)
        os.system('iconv -c -f GB2312 -t UTF-8 %s >> %s' % (elem, (elem[:-4])))
        os.system("mv %s '%s'" % (elem[:-4], new_dir))