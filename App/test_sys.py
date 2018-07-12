import sys

def test_1(input_list):
    print("len: "+ str(len(input_list)))
    for i in range(0,len(input_list)):
        print(input_list[i])

if __name__ == "__main__":
    test_1(sys.argv)
    