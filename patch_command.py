import sys
from function.shared_functions import *
import subprocess

def split_patch_name_without_path_and_diff(patch_name_path):
    begin_of_patch_name =patch_name_path.rfind('\\')+1
    end_of_patch_name =patch_name_path.rfind('.')
    new_path = patch_name_path[begin_of_patch_name:end_of_patch_name]
    return new_path
''''''
def scanAndApplyPatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory):
    append_time_string = generate_time_string()
    patch_files_list_origin = scan_all_directories_and_files(patchDirectory)
    
    start_index = len(patchDirectory)
    patch_files_list=[]
    path_files_relative_path=[]
    for temp_str in patch_files_list_origin:
        if temp_str.endswith('diff'):
            patch_files_list.append(temp_str)
            path_files_relative_path.append(temp_str[start_index+1:len(temp_str)-5])
            
    patch_files_list_len = len(patch_files_list)
    print(patch_files_list)
    print(path_files_relative_path)
    # traverse the file name and compare them
    for i in range(0,patch_files_list_len):
        # copy the origin file to the new directory
        create_a_directory_in_path(origCopyDirectory+append_time_string)
        user_files_name = sourceRootLevelDirectory+'\\'+path_files_relative_path[i]
#        print(user_files_name)
        temp_command_copy_string = "copy "+user_files_name+" "+origCopyDirectory+append_time_string
#        print(temp_command_copy_string)
        subprocess.Popen(temp_command_copy_string, shell=True, stdout=subprocess.PIPE).stdout.read()
        
        temp_command_patch_string = "patch "+user_files_name+" "+patch_files_list[i]
        print(temp_command_patch_string)
        print (subprocess.Popen(temp_command_patch_string, shell=True, stdout=subprocess.PIPE).stdout.read())
        

def check_input_parameter(input_list):
    '''check the input parameter...'''
    if len(input_list) >=4 :
        sourceRootLevelDirectory = handle_relative_path(input_list[1])
        patchDirectory = handle_relative_path(input_list[2])
        origCopyDirectory = handle_relative_path(input_list[3])
        sourceFileSpecList =[]
        for i in range(4,len(input_list)):
            sourceFileSpecList.append(input_list[i])
#        print(sourceFileSpecList)
        '''for now, we can ignore extensions of the file'''
        scanAndApplyPatches(sourceRootLevelDirectory,patchDirectory,origCopyDirectory)
    else :
        print("need more parameters! parameter 1~3 is path,parameter 4~n is file extension,such as: h cpp ")

if __name__ == '__main__':
    check_input_parameter(sys.argv)