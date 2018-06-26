import os
import subprocess

input_my_own_string = "diff D:\__project_data\diff_patch_directory\sourceRoot_modified\main.cpp D:\__project_data\diff_patch_directory\origCopy\main.cpp"
#print (subprocess.Popen(input_my_own_string, shell=True, stdout=subprocess.PIPE).stdout.read())
obj  = subprocess.Popen(input_my_own_string, shell=True, stdout=subprocess.PIPE)
print(obj.returncode)# it use this one, and I can get the result, then I can decide to do or not.

