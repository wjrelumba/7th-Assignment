# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

def userInput():
    sentence = input("Enter the sentence desired: ")
    return sentence

user = userInput()
consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
vowels = "AEIOUaeiou"
space = " "
consoWord = 0
vowelWord = 0
wordWord = 0

for cons in user:
    for consF in consonants:
        if cons == consF:
            consoWord = consoWord + 1

for vow in user:
    for vowF in vowels:
        if vow == vowF:
            vowelWord = vowelWord + 1

for spac in user:
    for spacF in space:
        if spac == spacF:
            wordWord = wordWord + 1
                                                                                        
print(f"Words:{wordWord + 1}")
print(f"Vowels:{vowelWord}")
print(f"Consonants:{consoWord}")