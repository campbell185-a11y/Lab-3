#this is how the user inputs the score
findScore = int(input("Enter a score: "))

#write a function that takes an exam score from 0 to 100 as a parameter
def findGrade(score):
    # I have these two first so it will check if it is below 0 or above 100
    if score < 0:
            return( "Error make score between 0 and 100")
    elif score > 100:
        return("Error make score between 0 and 100")
    elif score >= 90:
        return("A")
    elif score >= 80:
        return("B")
    elif score >= 70:
        return("C")
    elif score < 70:
        return("F")
    #executes the command
grade = findGrade(findScore)