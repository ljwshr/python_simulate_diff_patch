import datetime
import os

"""
INPUT:path string, such as "D:\\t\\Fire_Safety_Guide"
Return Value:string list,contains the all files's absolute path
"""
def scan_all_directories_and_files(root_path):
    return_list=[]#store the file path
    for absolute_path in os.walk(root_path):
        file_list_in_path_to_directory = absolute_path[2]
        the_num_of_files = len(file_list_in_path_to_directory)
        for i in range(0,the_num_of_files):
            tempRealPath = os.path.join(absolute_path[0],file_list_in_path_to_directory[i])
            return_list.append(tempRealPath)
    return return_list
"""
return a string of time, such as 2018712131600
"""
def generate_time_string():
    temp_my_time = datetime.datetime.now()
    result_date=""
    result_date+= str(temp_my_time.year)
    result_date+=str(temp_my_time.month)
    result_date+=str(temp_my_time.day)
    result_date+=str(temp_my_time.hour)
    result_date+=str(temp_my_time.minute)
    result_date+=str(temp_my_time.second)
    return result_date
"""
make directory with given path, if the path does not exist.
"""
def create_a_directory_in_path(path):
    folder = os.path.exists(path)  
    if not folder:                   #if exist
        os.makedirs(path)            #then make directory
        print ("the path does not exist, create new folder...")  
    else :
        print("just create the path for one time")
"""
split the longer string with the shorter string ,return (LongString - ShortString) 
"""        
def split_head(absolte_path_of_file,the_root_path):
    if len(absolte_path_of_file) > len(the_root_path):
        start_number =len(the_root_path)
        new_path = absolte_path_of_file[start_number:]
        return new_path
    else:
        print("the path is not right when split the path!!!!")
    return -1
        
"""
recurse the directory,and find files with same name
"""
def test_repeat_file(temp_Directory):
    file_list =scan_all_directories_and_files(temp_Directory)
    temp_list=[]
    my_dict_temp ={}
    repeat_files_list=[]
    file_name_repeat = "repeat_files"+generate_time_string()+".txt"
    file_record_process = open(file_name_repeat,'a+')
    for i in range(0,len(file_list)):
        temp_end = file_list[i].rfind('\\')
        temp_list.append(file_list[i][temp_end+1:]) 
        my_dict_temp[temp_list[i]]=i;
    
    for i in range(0,len(temp_list)):
        for j in range(i+1,len(temp_list)):
            if temp_list[i] == temp_list[j]:
                repeat_files_list.append(file_list[i])
                repeat_files_list.append(file_list[j])
                file_record_process.write(file_list[i]+"\n")
                file_record_process.write(file_list[j]+"\n")
                break
    file_record_process.close            
    print("the repeat_files length is: "+ str(len(repeat_files_list)))
    print("the list length is:  "+ str(len(file_list)))
    print("the dict length is:  "+ str(len(my_dict_temp)))
#    print(repeat_files_list)
    

"""
recurse the list,if the path end with given extension, then split the path with root_directory_string
"""    
def split_ralative_path_with_given_extension(absolute_path_list,given_extension_list,root_directory_string):
    # check if there is a space and split the ralative path list for further use
    relative_path_list =[]
    for i in range(0,len(absolute_path_list)):
        if absolute_path_list[i].find(" ") != -1:#find the space
            print("warning: the path contain a space,the path will be skipped: "+absolute_path_list[i]+"\n")
        else :
            temp_extension_index = absolute_path_list[i].rfind('.')
            temp_extension_of_file = absolute_path_list[i][temp_extension_index+1:]
            for traverse_str in given_extension_list:
                if temp_extension_of_file == traverse_str:
                    split_head_result=split_head(absolute_path_list[i],root_directory_string)
                    if split_head_result != -1:
                        relative_path_list.append(split_head_result)
                    break
    return relative_path_list
    