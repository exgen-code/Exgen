import random
from addition import addition
def readFile(fileName):
    # reads in the file, reads every line in the file using readLines
    # RETURNS 'What is $X + $Y equal to?'
    file = open(fileName, 'r') 
    contentFile = file.readlines()
    
    return contentFile[0]

def identifyVariables(question):
    # identifies the variables in the question
    variables = []
    hiddenConstants = []
    dictOfVars = {}
    # splits it up into words
    for i in question.split(" "):
        # if word starts with $, it's a variable
        if i[0] == "$":
            variableName = i.split('$')[1]
            variables.append(variableName)
            dictOfVars[variableName] = ""
    
    if len(question.split("{")) > 1:
        hiddenConstantsString = question.split("{")[1].split("}")[0]
        for constantDefinitions in  hiddenConstantsString.split(","):
            dictOfVars[constantDefinitions.split("=")[0]] = constantDefinitions.split("=")[1]
            
    return dictOfVars

def writeQuestion(question, answer, dictVariables):
    # TODO find some way so the user doesnt have to rewrite what the variables are here :)
    returnString = []

    if len(question.split("{")) > 1:
        question = question.split("{")[0] + question.split("}")[1]

    file_read = question.split(" ")
    for value in file_read:
        if value[0] != "$":
            returnString.append(value)
        else:
            if value[1] == "X":
                returnString.append(dictVariables['X'])
            if value[1] == "Y":
                returnString.append(dictVariables['Y'])
    returnString.append("\n " + str(answer))            

    return " ".join(str(x) for x in returnString)


a = readFile('example1.txt')
print("readFile is equal to", a)

additionQuestion = addition()
varDict = additionQuestion.generateNumbers(identifyVariables(a))
b,c = additionQuestion.generate(identifyVariables(a))
import pprint
pprint.pprint(b)
print("userChangeVariables is equal to", c)

question_complete = writeQuestion(a, c, b)
print(question_complete)
