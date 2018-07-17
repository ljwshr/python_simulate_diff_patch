import sys
from function.shared_functions import *
import subprocess


def scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory,sourceFileSpecList):
    global_change_count = 0
    file_name_string = "process"+generate_time_string()+".txt"
    file_record_process = open(file_name_string,'a+')
    ''' recurse the two Directory'''
    user_files_list = scan_all_directories_and_files(sourceRootLevelDirectory)
    origCopy_files_list = scan_all_directories_and_files(origCopyDirectory)
    user_files_list_len = len(user_files_list)
    print("user_files_list_len is: " + str(len(user_files_list)))
    file_record_process.write("user_files_list_len is: " + str(len(user_files_list))+"\n")
    print("origCopy_files_list_len is: " + str(len(origCopy_files_list)))
    file_record_process.write("origCopy_files_list_len is: " + str(len(origCopy_files_list))+"\n")
  
    if user_files_list_len == 0:
        print("the user files len is 0, please check your path !!!!!!!!!!")

    '''find the intersection files'''
    user_files_relative_path_list = split_ralative_path_with_given_extension(user_files_list,sourceFileSpecList,sourceRootLevelDirectory)
    origCopy_files_relative_path_list = split_ralative_path_with_given_extension(origCopy_files_list,sourceFileSpecList,origCopyDirectory)
    
    intersection_list=list(set(user_files_relative_path_list).intersection(set(origCopy_files_relative_path_list)))
    print("the intersection(the file with the same name) file number is  "+str(len(intersection_list)))
    file_record_process.write("the intersection(the file with the same name) file number is  "+str(len(intersection_list))+"\n")
 
    for i in range(0,len(intersection_list)):
        user_file_path_temp = sourceRootLevelDirectory+intersection_list[i]
        orig_file_path_temp = origCopyDirectory+intersection_list[i]
   
        temp_diff_string ="diff "+orig_file_path_temp+" "+user_file_path_temp
        print(str(i)+" -->times "+temp_diff_string)
        file_record_process.write(str(i)+" -->times "+temp_diff_string+"\n")
        result_of_command  = subprocess.Popen(temp_diff_string, shell=True, stdout=subprocess.PIPE)
        result_of_command.wait()# we must wait for the returncode result(0 or 1), otherwise, we will get None
        '''if there are differences, diff new file and backup original file'''
        if result_of_command.returncode == 1:
            global_change_count+=1
            print("OK,you should create a file")
            temp_diff_string +=" > "
            half_path = split_head(user_file_path_temp,sourceRootLevelDirectory)
            new_file_path = patchDirectory +"\\"+ half_path+".diff"
            #before execute this command,we should make this directory
            index_of_split = new_file_path.rfind('\\')
            the_path_that_will_create = new_file_path[:index_of_split]
      
            create_a_directory_in_path(the_path_that_will_create)
      
            temp_diff_string +=new_file_path+"\n"
            print(temp_diff_string)
            print (subprocess.Popen(temp_diff_string, shell=True, stdout=subprocess.PIPE).stdout.read())     
            temp_copy_string = "copy "+orig_file_path_temp+" "+the_path_that_will_create
            print(temp_copy_string)
            print (subprocess.Popen(temp_copy_string, shell=True, stdout=subprocess.PIPE).stdout.read())        

    # start to store the information to the file
    file_record_process.write(str(global_change_count)+" files have differences "+"\n")
    file_record_process.close       
# this is the end of the new method.

def check_input_parameter(input_list):
    '''check the input parameter...'''
    if len(input_list) >=4 :
        sourceRootLevelDirectory = handle_relative_path(input_list[1])
        patchDirectory = handle_relative_path(input_list[2])
        origCopyDirectory = handle_relative_path(input_list[3])
        sourceFileSpecList =[]
        for i in range(4,len(input_list)):
            sourceFileSpecList.append(input_list[i])
        print(sourceFileSpecList)
        scanAndCreatePatches(sourceRootLevelDirectory, patchDirectory, origCopyDirectory,sourceFileSpecList)
    else :
        print("need more parameters! parameter 1~3 is path,parameter 4~n is file extension,such as: h cpp ")
    
if __name__ == '__main__':
    check_input_parameter(sys.argv)