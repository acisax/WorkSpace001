'''
Created on 2013-6-10

@author: Charles
'''
import os

path_want = r'D:\PROJECT_SPACE\PYTHON_SPACE\log_test'
before_str = r'20130609'
after_str = r'20130610'

for cur_path, dir_list, file_list in os.walk(path_want) :
    print(r'DIRECTORY----' + cur_path + r'----Replaced Start...')
    for i_file in file_list :
        ifile_fullname = cur_path + '\\' + i_file
        in_file = open(ifile_fullname)
        all_lines = in_file.readlines()
        in_file.close()
         
        out_file = open(ifile_fullname, 'w')
        for j_line in all_lines:
            if not j_line:
                break
            if before_str in j_line:
                modified_str = j_line.replace(before_str, after_str)
                out_file.write(modified_str)
            else:
                out_file.write(j_line)
        out_file.close()
        print(r'FILE--' + ifile_fullname + r'--Replaced OK !')
    print(r'DIRECTORY----' + cur_path + r'----Replaced OK !\n\n')