
my_string = "D:\__project_data\diff_patch_directory\sourceRoot_modified\main.cpp"
root_string = "D:\__project_data"

# the_len=len(root_string)
# print(the_len)
# temp = my_string.rfind('\\')
# my_new_string = my_string[the_len:temp]
# print(my_new_string)

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

test = split_head_tail(my_string,root_string)
print(test)
    