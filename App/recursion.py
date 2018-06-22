import os
from _overlapped import NULL

#rootdir = 'D:\\t\\Fire_Safety_Guide'


def scan_all_directories_and_files(root_path='D:\\t\\Fire_Safety_Guide'):
    root_path_list = os.listdir(root_path)
    return_list=[]#store the file path
    #print(isinstance(root_path_list, list))
    for absolute_path in os.walk(root_path):
        print(absolute_path)
        
        path_to_directory = absolute_path[0]#get the first path
        file_list_in_path_to_directory = absolute_path[2]
        the_num_of_files = len(file_list_in_path_to_directory)
        
        for i in range(0,the_num_of_files):
            tempRealPath = os.path.join(absolute_path[0],file_list_in_path_to_directory[i])
            #print(tempRealPath)
            return_list.append(tempRealPath)
    return return_list

My_list=[]          
My_list = scan_all_directories_and_files()
print(My_list)