#how the user can enter in a sentence
myString = input("Please put in a sentence for spaces to be removed: ")

def stripSpaces(myString):
    #makes the new string
    newStr = ""
    for ch in myString:
        #checks if the character is not a space
        if ch != " ":
            newStr = newStr + ch
    return (newStr)
#assigns the function to noSpaces
noSpaces = stripSpaces(myString)
#prints the sentence plus no spaces with the ran function
print("Phrase without spaces  : ", noSpaces )  


