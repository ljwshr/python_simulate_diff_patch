import os
import subprocess
from test.test_decimal import directory
import datetime


patchDirectory = "D:\\__project_data\\diff_real_project\\working\\"
sourceRootLevelDirectory = "D:\\__project_data\\diff_real_project\\git-AD18-UT-Tests3\\AD18-EN\\build"
origCopyDirectory="D:\\__project_data\\diff_real_project\\git-AD18\\AD18-EN\\build"
sourceFileSpecList=["h","cpp"]

create_directory_flag = True
global_store_string =""
global_change_count=0

def split_head(absolte_path_of_file,the_root_path):
    if len(absolte_path_of_file) > len(the_root_path):
        start_number =len(the_root_path)
        new_path = absolte_path_of_file[start_number:]
        return new_path
    else:
        print("the path is not right when split the path!!!!")
    return -1

def split_head_tail(absolte_path_of_file,the_root_path):
    global global_store_string
    if len(absolte_path_of_file) > len(the_root_path):
        #end_number=absolte_path_of_file.rfind('\\')
        start_number =len(the_root_path)+1
        new_path_will_created = absolte_path_of_file[start_number:]
        return new_path_will_created
    else:
        print("the path is not right when split the path!!!!")
        global_store_string +="the path is not right when split the path!!!!"
    return ""

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
INPUT:path string, such as "D:\\t\\Fire_Safety_Guide"
Return Value:string list,contains the all files's absolute path
"""
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
  
    
"""
INPUT:path string
OUTPUT:none
ATTENTIOINS:
we should use "\\" instead of "\" in the path
"""
#be careful, when to create a fiel, the path should be specially treated.
def create_a_directory_in_path(path):
    global create_directory_flag
    folder = os.path.exists(path)  
    if not folder:                   #if exist
        os.makedirs(path)            #then make directory
        print ("--- the path is not exist, create new folder...  ---")  
        create_directory_flag = False    
    else: 
        if  create_directory_flag == True:
            print ("--- Warning: This path exists, so I won't create a new directory  ---" )
        else:
            print("--- This is the My Own folder,just create one more ---")
"""
Inputs:
    1.sourceRootLevelDirectory: the directory that is modified by user.
    2.patchDirectory: the directory that not exist,and will store the diff file.
    3.origCopyDirectory: the directory that contains original files.
Return Value: None
Fucntion describe:
    1. scan the sourceRootLevelDirectory recursively, and store all the paths of the file in a list.
    2. traverse the list,and generate a batch command line. the command line is to find the difference of the files.
    3. execute the command, and store the differences in a new file.

"""  
def scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory,sourceFileSpecList):
    global global_store_string
    file_name_string = "process"+generate_time_string()+".txt"
    file_record_process = open(file_name_string,'a+')
    """
    recurse the two Directory, and find the differenct
    """
    user_files_list = scan_all_directories_and_files(sourceRootLevelDirectory)
    origCopy_files_list = scan_all_directories_and_files(origCopyDirectory)
    user_files_list_len = len(user_files_list)
    print("user_files_list_len is: " + str(len(user_files_list)))
    file_record_process.write("user_files_list_len is: " + str(len(user_files_list))+"\n")
    print("origCopy_files_list_len is: " + str(len(origCopy_files_list)))
    file_record_process.write("origCopy_files_list_len is: " + str(len(origCopy_files_list))+"\n")
    """
    These are pre-conditions:
        1. the length should be larger than 0
        2. the file number of the two diretory should be equal
    """
    if user_files_list_len == 0:
        print("the user files len is 0, please check your path !!!!!!!!!!")
        global_store_string +="the user files len is 0, please check your path !!!!!!!!!!"

    # check the intersection
    user_files_relative_path_list = []
    origCopy_files_relative_path_list = []
    # check if there is a space and split the ralative path list for further use
    for i in range(0,len(user_files_list)):
        if user_files_list[i].find(" ") != -1:#find the space
            file_record_process.write("warning: the path contain a space,the path will be skipped: "+user_files_list[i]+"\n")
        else :
            temp_extension_index = user_files_list[i].rfind('.')
            temp_extension_of_file = user_files_list[i][temp_extension_index+1:]
            for traverse_str in sourceFileSpecList:
                if temp_extension_of_file == traverse_str:
                    split_head_result=split_head(user_files_list[i],sourceRootLevelDirectory)
                    if split_head_result != -1:
                        user_files_relative_path_list.append(split_head_result)
                    break
            
            
    for i in range(0,len(origCopy_files_list)):
        if origCopy_files_list[i].find(" ") != -1:#find the space
            file_record_process.write("warning: the path contain a space,the path will be skipped: "+origCopy_files_list[i]+"\n")
        else :
            temp_extension_index = origCopy_files_list[i].rfind('.')
            temp_extension_of_file = origCopy_files_list[i][temp_extension_index+1:]
            for traverse_str in sourceFileSpecList:
                if temp_extension_of_file == traverse_str:
                    split_head_result=split_head(origCopy_files_list[i],origCopyDirectory)
                    if split_head_result != -1:
                        origCopy_files_relative_path_list.append(split_head_result)
                    break
    
#     print(len(user_files_relative_path_list))
#     print(len(origCopy_files_relative_path_list))
    intersection_list=list(set(user_files_relative_path_list).intersection(set(origCopy_files_relative_path_list)))
    print("the intersection(the file with the same name) file number is  "+str(len(intersection_list)))
    file_record_process.write("the intersection(the file with the same name) file number is  "+str(len(intersection_list))+"\n")
    differen_set_1 = list(set(user_files_relative_path_list).difference(set(origCopy_files_relative_path_list)))
    print(len(differen_set_1))
    differen_set_2 = list(set(origCopy_files_relative_path_list).difference(set(user_files_relative_path_list)))
    print(len(differen_set_2))   

    for i in range(0,len(intersection_list)):
        user_file_path_temp = sourceRootLevelDirectory+intersection_list[i]
        orig_file_path_temp = origCopyDirectory+intersection_list[i]

        
#this is begin of new method    
        temp_diff_string ="diff "+orig_file_path_temp+" "+user_file_path_temp
        print(str(i)+" -->times "+temp_diff_string)
        file_record_process.write(str(i)+" -->times "+temp_diff_string+"\n")
        global_store_string +=temp_diff_string
        result_of_command  = subprocess.Popen(temp_diff_string, shell=True, stdout=subprocess.PIPE)
        result_of_command.wait()# we must wait for the returncode result(0 or 1), otherwise, we will get None
#        print(result_of_command.returncode)
        if result_of_command.returncode == 1:
            print("OK,you should create a file")
            global global_change_count
            global_change_count+=1
            temp_diff_string +=" > "
            #the begin: just copy the codes from the old version
            half_path = split_head_tail(user_file_path_temp,sourceRootLevelDirectory)
      
            new_file_path = patchDirectory + half_path+".diff"
            #before execute this command,we should make this directory
            index_of_split = new_file_path.rfind('\\')
            the_path_that_will_create = new_file_path[:index_of_split]
      
            create_a_directory_in_path(the_path_that_will_create)
      
            temp_diff_string +=new_file_path+"\n"
            print(temp_diff_string)
            print (subprocess.Popen(temp_diff_string, shell=True, stdout=subprocess.PIPE).stdout.read())     
            temp_copy_string = "copy "+orig_file_path_temp+" "+the_path_that_will_create
            print(temp_copy_string)
            print (subprocess.Popen(temp_copy_string, shell=True, stdout=subprocess.PIPE).stdout.read())        
            #the end 
    # start to store the information to the file
    file_record_process.write(str(global_change_count)+" files have differences "+"\n")
    file_record_process.close       
# this is the end of the new method.
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
    print(repeat_files_list)


test_repeat_file(sourceRootLevelDirectory)
test_repeat_file(origCopyDirectory)
       
scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory,sourceFileSpecList)




    

