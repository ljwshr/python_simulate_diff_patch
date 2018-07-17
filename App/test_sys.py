import sys
import os

string1 = "D:\__project_data\diff_real_project\git-AD18\AD18-EN\build"

def test_1(input_list):
    print("len: "+ str(len(input_list)))
    for i in range(0,len(input_list)):
        print(input_list[i])
    print(os.getcwd())
def test_2():
    print(50*"*")
    print(string1)

if __name__ == "__main__":
    test_1(sys.argv)
    print(os.name)
    test_2()