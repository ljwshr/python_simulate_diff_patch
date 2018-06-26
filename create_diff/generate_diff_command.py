import os
import subprocess
from test.test_decimal import directory
patchDirectory = "D:\\__project_data\\diff_patch_directory\\working\\"
sourceRootLevelDirectory = "D:\__project_data\diff_patch_directory\sourceRoot_modified"
origCopyDirectory="D:\__project_data\diff_patch_directory\origCopy"
command_name = "command_generated_by_python"
public_long_string=""
create_directory_flag = True


def split_head_tail(absolte_path_of_file,the_root_path):
    if len(absolte_path_of_file) > len(the_root_path):
        #end_number=absolte_path_of_file.rfind('\\')
        start_number =len(the_root_path)+1
        new_path_will_created = absolte_path_of_file[start_number:]
        return new_path_will_created
    else:
        print("the path is not right when split the path!!!!")
    return ""

"""
INPUT:path string, such as "D:\\t\\Fire_Safety_Guide"
Return Value:string list,contains the all files's absolute path
"""
def scan_all_directories_and_files(root_path='D:\\t\\Fire_Safety_Guide'):
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
def scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory):
    """
    recurse the two Directory, and find the differenct
    """
    global public_long_string
    user_files_list = scan_all_directories_and_files(sourceRootLevelDirectory)
    origCopy_files_list = scan_all_directories_and_files(origCopyDirectory)
    user_files_list_len = len(user_files_list)
#    temp_string = str(user_files_list_len)
    if len(user_files_list) != len(origCopy_files_list):
        print("the number of the files in two Direcotory is not equal"+50*"!")
        print("program exit")
        return 1
    
    for i in range(0,user_files_list_len):
        user_file_path_temp = user_files_list[i]
        orig_file_path_temp = origCopy_files_list[i]

        
#this is begin of new method    
        temp_diff_string ="diff "+user_file_path_temp+" "+orig_file_path_temp
        print(temp_diff_string)
        result_of_command  = subprocess.Popen(temp_diff_string, shell=True, stdout=subprocess.PIPE)
        result_of_command.wait()# we must wait for the returncode result(0 or 1), otherwise, we will get None
        print(result_of_command.returncode)
        if result_of_command.returncode == 1:
            print("OK,you should create a file")
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
            public_long_string += temp_diff_string
            print (subprocess.Popen(temp_diff_string, shell=True, stdout=subprocess.PIPE).stdout.read())     
            temp_copy_string = "copy "+orig_file_path_temp+" "+the_path_that_will_create
            print(temp_copy_string)
            public_long_string += temp_copy_string
            print (subprocess.Popen(temp_copy_string, shell=True, stdout=subprocess.PIPE).stdout.read())
            #the end 
  
        else :
            print("No, you should not create a file")

        
# this is the end of the new method.


#this is the begin of old method (create all the diff files)

#         print(user_file_path_temp)
#         print(orig_file_path_temp)
#         temp_diff_string ="diff "+user_file_path_temp+" "+orig_file_path_temp+" > "        
#         half_path = split_head_tail(user_file_path_temp,sourceRootLevelDirectory)
# 
#         new_file_path = patchDirectory + half_path+".diff"
#         #before execute this command,we should make this directory
#         index_of_split = new_file_path.rfind('\\')
#         the_path_that_will_create = new_file_path[:index_of_split]
# 
#         create_a_directory_in_path(the_path_that_will_create)
# 
#         temp_diff_string +=new_file_path+"\n"
#         print(temp_diff_string)
#         public_long_string += temp_diff_string
#         print (subprocess.Popen(temp_diff_string, shell=True, stdout=subprocess.PIPE).stdout.read())     
#         temp_copy_string = "copy "+orig_file_path_temp+" "+the_path_that_will_create
#         print(temp_copy_string)
#         public_long_string += temp_copy_string
#         print (subprocess.Popen(temp_copy_string, shell=True, stdout=subprocess.PIPE).stdout.read())
    
#this is the end of old method        


        
scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory)




    

