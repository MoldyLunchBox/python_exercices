import sys
if (len(sys.argv) >= 2):
    sys.argv.pop(0)
    sys.argv = " ".join(str(x) for x in sys.argv)
    print(sys.argv[::-1].swapcase())
