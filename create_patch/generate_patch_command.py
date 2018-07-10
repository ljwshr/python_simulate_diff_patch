import os
import subprocess
sourceRootLevelDirectory = "D:\\__project_data\\apply_patchs_real_project\\git-AD18\\AD18-EN\\build"
patchDirectory = "D:\\__project_data\\apply_patchs_real_project\\patchs"
origCopyDirectory = "D:\\__project_data\\apply_patchs_real_project\\backup"

create_directory_flag = True

import datetime
from builtins import str


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
        
        file_list_in_path_to_directory = absolute_path[2]
        the_num_of_files = len(file_list_in_path_to_directory)
        
        for i in range(0,the_num_of_files):
            tempRealPath = os.path.join(absolute_path[0],file_list_in_path_to_directory[i])
            #print(tempRealPath)
            return_list.append(tempRealPath)
    return return_list

def split_patch_name_without_path_and_diff(patch_name_path):
    begin_of_patch_name =patch_name_path.rfind('\\')+1
    end_of_patch_name =patch_name_path.rfind('.')
    new_path = patch_name_path[begin_of_patch_name:end_of_patch_name]
    return new_path

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

def scanAndApplyPatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory):
    #scan the SourceRootLevelDirectory recursively and store the results in a list(bigger list).
    user_files_list = scan_all_directories_and_files(sourceRootLevelDirectory)
    user_files_list_len = len(user_files_list)
    append_time_string = generate_time_string()

    #scan the patchDirectory, and store the results in a list(smaller list).
    patch_files_list = scan_all_directories_and_files(patchDirectory)
    patch_files_list_len = len(patch_files_list)
    # traverse the file name and compare them
    for i in range(0,patch_files_list_len):
        patch_name_pure=split_patch_name_without_path_and_diff(patch_files_list[i])
        
        for j in range(0,user_files_list_len):
            begin_of_file_name=user_files_list[j].rfind('\\')+1
            temp_user_file_name = user_files_list[j][begin_of_file_name:]
            if patch_name_pure == temp_user_file_name:
                # copy the origin file to the new directory
                
                create_a_directory_in_path(origCopyDirectory+append_time_string)
                temp_command_copy_string = "copy "+user_files_list[j]+" "+origCopyDirectory+append_time_string
#                 print(temp_command_string)
                print (subprocess.Popen(temp_command_copy_string, shell=True, stdout=subprocess.PIPE).stdout.read())
                #generate the command string
                temp_command_patch_string = "patch "+user_files_list[j]+" "+patch_files_list[i]
                print(temp_command_patch_string)
                print (subprocess.Popen(temp_command_patch_string, shell=True, stdout=subprocess.PIPE).stdout.read())
             
#                 print("OK")
                break
#             else:
#                 print("not ok")
                
                
scanAndApplyPatches(sourceRootLevelDirectory,patchDirectory,origCopyDirectory)
                
    