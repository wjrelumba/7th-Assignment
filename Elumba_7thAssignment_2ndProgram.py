# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid
# Tip: loop through each character of the input then process it letter by letter

def userInput():
    passwordF = input("Enter your password please: ")
    return passwordF

def capLetterAuthenticate(passwordF, capLetterF):
    for capLF in passwordF:
        for capL in capLetter:
            if capLF == capL:
                capLetterF = capLetterF + 1
    return capLetterF

def numberAuthenticate(passwordF, numberF):
    for numF in passwordF:
        for num in number:
            if numF == num:
                numberF = numberF + 1
    return numberF

def specCharacterAuthenticate(passwordF, specCharF):
    for specCF in passwordF:
        for specC in specChar:
            if specCF == specC:
                specCharF = specCharF + 1
    return specCharF

password = userInput()
capLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
specChar = "!@#$%^&*()-_+=/?\|,.<>"
passWlength = len(password)
capLetterNum = 0
numberNum = 0
specCharNum = 0

if passWlength > 15:
    capLetterValue = capLetterAuthenticate(password, capLetterNum)
else:
    capLetterValue = 0
                                 
if capLetterValue >= 1:
    numberValue = numberAuthenticate(password, numberNum)
else:
    numberValue = 0
        
if numberValue >= 1:
    specCharValue = specCharacterAuthenticate(password, specCharNum)
else:
    specCharValue = 0
            
if specCharValue >= 1:
    print("Valid")
else:
    print("Invalid")