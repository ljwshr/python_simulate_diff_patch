import os
import subprocess
from test.test_decimal import directory
patchDirectory = "D:\\__project_data\\diff_patch_directory\\working\\"
sourceRootLevelDirectory = "D:\__project_data\diff_patch_directory\sourceRoot_modified"
origCopyDirectory="D:\__project_data\diff_patch_directory\origCopy"
command_name = "command_generated_by_python"
temp_string="echo off\n"+"rm -rf working\n"+"mkdir working\n\n"+"diff "

def execute_the_bat_file():
    os.chdir(patchDirectory)
    os.startfile(command_name+".bat")
#be careful, when to create a fiel, the path should be specially treated.
def create_a_directory_in_path(path):
    folder = os.path.exists(path)  

    if not folder:                   #if exist
        os.makedirs(path)            #then make directory
        print ("---  new folder...  ---")  
        print ("---  OK  ---")  
  
    else:  
        print ("---  There is this folder!  ---" )
    #create a file
#     file = open(path + command_name + '.bat','w')
#     file.write(input_string)   
#     file.close()  

def scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory):
    directory_list = os.listdir(sourceRootLevelDirectory)# search the list
#    print(isinstance(directory_list, list))
    temp_string1 = temp_string + sourceRootLevelDirectory +"\\" +directory_list[0]+" "
    temp_file1 = sourceRootLevelDirectory +"\\" +directory_list[0]+" "
    
    directory_list2 = os.listdir(origCopyDirectory)
    temp_string2 = origCopyDirectory+"\\" + directory_list2[0]
#    print(temp_string2)
    
    temp_string1 += temp_string2
    temp_string1 += " > "+"working\working.diff\n\n"
    temp_string1 +="copy origCopy\main.cpp working\n\n"
    temp_string1 +="echo end"
    print(temp_string1)
    
# run the command directly
#     create_a_directory_in_path(patchDirectory)
#     command_one = "diff D:\__project_data\diff_patch_directory\sourceRoot_modified\main.cpp D:\__project_data\diff_patch_directory\origCopy\main.cpp > D:\__project_data\diff_patch_directory\working\working.diff"
#     print (subprocess.Popen(command_one, shell=True, stdout=subprocess.PIPE).stdout.read())
    command_two = "copy "+temp_file1+" "+patchDirectory
    print(command_two)
    print (subprocess.Popen(command_two, shell=True, stdout=subprocess.PIPE).stdout.read())
    
    
#    print (subprocess.Popen(temp_string1, shell=True, stdout=subprocess.PIPE).stdout.read())
    
#    create_string_for_command(temp_string1,patchDirectory)
#    execute_the_bat_file()
        
scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory)




    

