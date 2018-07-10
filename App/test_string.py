

my_string = "D:\__project_data\diff_patch_directory\sourceRoot_modified\main.cpp"
root_string = "D:\__project_data"


"""
Attention: should check the length,here may a bug,when there is nothing to create
"""
def split_head_tail(absolte_path_of_file,the_root_path):
    if len(absolte_path_of_file) > len(the_root_path):
        end_number=absolte_path_of_file.rfind('\\')
        start_number =len(the_root_path)
        new_path_will_created = absolte_path_of_file[start_number:end_number]
        return new_path_will_created
    else:
        print("the path is not right when split the path!!!!")
    return ""

# test = split_head_tail(my_string,root_string)
# print(test)
"""
if wrong,it return a int number
if right,it return a string
"""
def split_head(absolte_path_of_file,the_root_path):
    if len(absolte_path_of_file) > len(the_root_path):
        start_number =len(the_root_path)
        new_path_will_created = absolte_path_of_file[start_number:]
        return new_path_will_created
    else:
        print("the path is not right when split the path!!!!")
    return -1

# test = split_head(my_string,root_string)
# print(test == -1)
# print(test)
    
sourceFileSpecList=["h","*cpp"]
temp_string = "D:\__project_data\diff_real_project\git-AD18\AD18-EN\build\gtest\googletest\samples\sample1.h"
end_string_temp = temp_string.rfind('.')
print(end_string_temp)
temp_extension = temp_string[end_string_temp+1:]
print(temp_string[end_string_temp+1:])
for str in sourceFileSpecList:
    if temp_extension == str:
        print("OK")