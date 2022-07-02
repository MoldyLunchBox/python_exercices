import string

def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if (len(args) == 0):
        val = input('What is the text to analyse?\n')
        text_analyzer(val)
    elif (len(args) > 1):
        print('ERROR')
    else:
        puncs = string.punctuation
        pun = 0
        upper = 0
        lower = 0
        for char in args[0]:
            if (char in puncs):
                pun += 1
            elif (char.isupper() == True):
                upper += 1
            elif (char.islower() == True):
                lower += 1
        print ("-", upper, "upper letters")
        print ("-", lower, "lower letters")
        print ("-", pun, "punctuation marks")
        print ("-", args[0].count(' '), "spaces")