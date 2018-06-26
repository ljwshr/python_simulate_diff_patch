patch_name_path = "D:\__project_data\apply_patch_directory\patchs\main.cpp.diff"


def split_patch_name_without_path(patch_name_path):
    begin_of_patch_name =patch_name_path.rfind('\\')+1
    end_of_patch_name =patch_name_path.rfind('.')
    new_path = patch_name_path[begin_of_patch_name:end_of_patch_name]
    return new_path
    
result_split=split_patch_name_without_path(patch_name_path)
print(result_split)
    
    