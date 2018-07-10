import sys
import os

patchDirectory = "D:\\__project_data\\diff_real_project\\working\\"
sourceRootLevelDirectory = "D:\\__project_data\\diff_real_project\\git-AD18-UT-Tests3\\AD18-EN\\build"
origCopyDirectory="D:\\__project_data\\diff_real_project\\git-AD18\\AD18-EN\\build"

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

def split_head(absolte_path_of_file,the_root_path):
    if len(absolte_path_of_file) > len(the_root_path):
        start_number =len(the_root_path)
        new_path = absolte_path_of_file[start_number:]
        return new_path
    else:
        print("the path is not right when split the path!!!!")
    return -1

def test_input_files(sourceRootLevelDirectory, patchDirectory, origCopyDirectory):
    user_files_list = scan_all_directories_and_files(sourceRootLevelDirectory)
    origCopy_files_list = scan_all_directories_and_files(origCopyDirectory)
    print("user_files_list_len is: " + str(len(user_files_list)))
    print("origCopy_files_list_len is: " + str(len(origCopy_files_list)))
    
    # check the intersection
    user_files_relative_path_list = []
    origCopy_files_relative_path_list = []
    # check if there is a space and split the ralative path list for further use
    for i in range(0,len(user_files_list)):
        if user_files_list[i].find(" ") != -1:#find the space
            print("wrong")
            return "the --> "+sourceRootLevelDirectory+" <-- contains space !!"
        else :
            split_head_result=split_head(user_files_list[i],sourceRootLevelDirectory)
            if split_head_result != -1:
                user_files_relative_path_list.append(split_head_result)
            
    for i in range(0,len(origCopy_files_list)):
        if origCopy_files_list[i].find(" ") != -1:#find the space
            print("wrong")
            return "the --> "+origCopyDirectory+" <-- contains space !!"
        else :
            split_head_result=split_head(origCopy_files_list[i],origCopyDirectory)
            if split_head_result != -1:
                origCopy_files_relative_path_list.append(split_head_result)
    
#     print(len(user_files_relative_path_list))
#     print(len(origCopy_files_relative_path_list))
    intersection_list=list(set(user_files_relative_path_list).intersection(set(origCopy_files_relative_path_list)))
    print("the intersection(the file with the same name) file number is  "+str(len(intersection_list)))
    differen_set_1 = list(set(user_files_relative_path_list).difference(set(origCopy_files_relative_path_list)))
    print(differen_set_1)
    differen_set_2 = list(set(origCopy_files_relative_path_list).difference(set(user_files_relative_path_list)))
    print(len(differen_set_2))
    
    
    
    
            
        
    
    
        
        
        
    
    
    
if __name__ == "__main__":
    sys.exit(test_input_files(sourceRootLevelDirectory, patchDirectory, origCopyDirectory))