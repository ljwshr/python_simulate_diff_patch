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
#         print(user_file_path_temp)
#         print(orig_file_path_temp)
        temp_diff_string ="diff "+user_file_path_temp+" "+orig_file_path_temp+" > "
        
        half_path = split_head_tail(user_file_path_temp,sourceRootLevelDirectory)
#         print(half_path)
        new_file_path = patchDirectory + half_path+".diff"
        #before execute this command,we should make this directory
        index_of_split = new_file_path.rfind('\\')
        the_path_that_will_create = new_file_path[:index_of_split]
#        print(the_path_that_will_create)
        create_a_directory_in_path(the_path_that_will_create)
#         print(new_folder_file_path)
        temp_diff_string +=new_file_path+"\n"
        print(temp_diff_string)
        public_long_string += temp_diff_string
        print (subprocess.Popen(temp_diff_string, shell=True, stdout=subprocess.PIPE).stdout.read())
        
        temp_copy_string = "copy "+orig_file_path_temp+" "+the_path_that_will_create
        print(temp_copy_string)
        public_long_string += temp_copy_string
        print (subprocess.Popen(temp_copy_string, shell=True, stdout=subprocess.PIPE).stdout.read())
    
        
            
        
        
        
  
         
        
    
#     directory_list = os.listdir(sourceRootLevelDirectory)# search the list
#     temp_string1 = temp_string + sourceRootLevelDirectory +"\\" +directory_list[0]+" "
#     temp_file1 = sourceRootLevelDirectory +"\\" +directory_list[0]+" "
#     
#     directory_list2 = os.listdir(origCopyDirectory)
#     temp_string2 = origCopyDirectory+"\\" + directory_list2[0]
# #    print(temp_string2)
#     
#     temp_string1 += temp_string2
#     temp_string1 += " > "+"working\working.diff\n\n"
#     temp_string1 +="copy origCopy\main.cpp working\n\n"
#     temp_string1 +="echo end"
#     print(temp_string1)
    
# run the command directly
#     create_a_directory_in_path(patchDirectory)
#     command_one = "diff D:\__project_data\diff_patch_directory\sourceRoot_modified\main.cpp D:\__project_data\diff_patch_directory\origCopy\main.cpp > D:\__project_data\diff_patch_directory\working\working.diff"
#     print (subprocess.Popen(command_one, shell=True, stdout=subprocess.PIPE).stdout.read())

#     command_two = "copy "+temp_file1+" "+patchDirectory
#     print(command_two)
#     print (subprocess.Popen(command_two, shell=True, stdout=subprocess.PIPE).stdout.read())
    

        
scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory)




    

