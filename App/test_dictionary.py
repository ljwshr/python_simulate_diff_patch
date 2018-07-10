# my_list = ["ljw","ljw1","ljw2","Siemens","ljw1"]
# my_dict ={}
# for i in range(0,len(my_list)):
#     my_dict[my_list[i]]=i;
# print(my_dict)
# print(len(my_dict))

import os
def scan_all_directories_and_files(root_path):
    return_list=[]#store the file path
    #print(isinstance(root_path_list, list))
    for absolute_path in os.walk(root_path):
        #print(absolute_path)
        
        file_list_in_path_to_directory = absolute_path[2]
        the_num_of_files = len(file_list_in_path_to_directory)
        
        for i in range(0,the_num_of_files):
            tempRealPath = os.path.join(absolute_path[0],file_list_in_path_to_directory[i])
            #print(tempRealPath)
            return_list.append(tempRealPath)
    return return_list


    
if __name__ == "__main__":
    test_repeat_file()
    