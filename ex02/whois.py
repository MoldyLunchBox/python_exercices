import sys
if (len(sys.argv) > 2):
    print("AssertionError: more than one argument is provided")
elif(len(sys.argv) == 2):
    if ((sys.argv[1].isdigit()) == False):
        print("AssertionError: argument is not integer")
    elif (int(sys.argv[1]) % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
