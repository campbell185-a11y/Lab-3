myString = input("Please put in a sentence for spaces to be removed: ")

def stripSpaces(myString):
    newStr = ""
    for ch in myString:
        if ch != " ":
            newStr = newStr + ch
    return (newStr)
noSpaces = stripSpaces(myString)

return("Phrase without spaces  : ", noSpaces )  
