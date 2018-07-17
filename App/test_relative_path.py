import os
import sys

def test_relative_path(input_string):
    
    real_absolute_path =""
    if os.name == 'nt':# this is windows system
        print(os.getcwd()+'\\'+input_string)
        print(input_string.find(':'))
        if input_string.find(':') == -1:
            print("this is an relative path")
            split_character_list = input_string.split('/')#only need to split the  '/' , if it is '\',no need to split,just append it
            real_absolute_path = os.getcwd()
            print(split_character_list)
            back_path_step = 0#how many steps should be backward
            for i in range(len(split_character_list)):#calculate the steps
                if split_character_list[i] != '..':
                    back_path_step = i
                    break
            for i in range(back_path_step):#
                start_index=real_absolute_path.rfind('\\')
                real_absolute_path = real_absolute_path[:start_index]
                
            for i in range(back_path_step,len(split_character_list)):
                real_absolute_path += '\\' + split_character_list[i]
            print(real_absolute_path)
        else:
            print("this is an absolute path")
            real_absolute_path = input_string
            
        return real_absolute_path
    
    
if __name__ =='__main__':
    test_relative_path("../../a/b/c")