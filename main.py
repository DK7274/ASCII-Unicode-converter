#function to convert ASCII to Unicode
def ASCIIUnicodeConvert():
    #retrieves userinput from new line
    userInput = input("input ASCII\n> ")
    #makes you try again if you dont put in an ASCII character
    if not userInput.isascii():
        print("invalid ASCII input, try again")
        ASCIIUnicodeConvert()
    if userInput < 0:
        print("invalid ASCII input, try again")
        ASCIIUnicodeConvert()
    #converts ASCII character to unicode character
    print(chr(userInput))
    #returns you to the main function
    start()


#function to convert Unicode to ASCII
def UnicodeASCIIConvert():
    userInput = input("input Unicode\n> ")
    #starts an array
    if len(userInput) > 1:
        inputArray = []
        #ord command can only process one digit at a time, so this for loop goes through each digit and converts it that way
        for a in userInput:
            inputArray.append(ord(a))
        #prints ASCII and returns it to start function
        print(''.join(inputArray))
        start()
    #if nothing inputted return to start of this function
    elif len(userInput) == 0:
        print("invalid Unicode input, try again")
        UnicodeASCIIConvert()
    print(ord(userInput))
    start()

#initial body of code, asks whether want to convert from ASCII to Unicode, or Unicode to ASCII
def start():
    #shows name of program and gets input for whether they want to use ASCII or unicode converter
    print("ASCII-Unicode converter")
    userInput = input("For ASCII -> Unicode type Unicode\nFor Unicode -> ASCII type ASCII\n> ")
    if userInput == "Unicode":
        ASCIIUnicodeConvert()
    elif userInput == "ASCII":
        UnicodeASCIIConvert()
    #invalid input returns them to start of program to try again
    else:
        print("invalid input, try again")
        start()



#starts running the start function
start()