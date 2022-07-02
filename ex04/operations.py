import string
import sys

if (len(sys.argv) != 3 or sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False):
    print "Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3"
else:
    print "Sum:       ", int(sys.argv[1]) + int(sys.argv[2])
    print "Difference:", int(sys.argv[1]) - int(sys.argv[2])
    print "Product:   ", int(sys.argv[1]) * int(sys.argv[2])
    if (sys.argv[2] is '0'):
        print "Quotient:   ERROR (div by zero)"
    else:
        print "Quotient:  ", float(sys.argv[1]) / float(sys.argv[2])
    if (sys.argv[2] is '0'):
        print "Remainder:  ERROR (div by zero)"
    else:
        print "Remainder: ", int(sys.argv[1]) % int(sys.argv[2])


        