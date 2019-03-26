from addition import addition
from random import shuffle
import pprint


def readFile(fileName):
    """ reads in the file, reads every line in the file using readLines
    RETURNS 'What is $X + $Y equal to?'
    """
    file = open(fileName, 'r')
    contentFile = file.readlines()

    return contentFile[0]


def identifyVariables(question):
    """identifies the variables in the question"""
    variables = []
    dictOfVars = {}
    # splits it up into words
    for i in question.split(" "):
        # if word starts with $, it's a variable
        if i[0] == "$":
            variableName = i.split('$')[1]
            variables.append(variableName)
            dictOfVars[variableName] = ""

    # If there is a '{' in the question, there are hidden constants in
    # the question
    if len(question.split("{")) > 1:
        # Everything between a { and a } is a series of definitions of
        # hidden contants
        hiddenConstantsString = question.split("{")[1].split("}")[0]
        # Hiddent constant definitions are comma separated
        for constantDefinitions in \
                hiddenConstantsString.replace(' ', '').split(","):
            # Whatever is on the left of the '=' is the name (key) of
            # the constant and whatever is in the right is the value
            # Add them to the dictionary
            dictOfVars[constantDefinitions.split("=")[0]] \
                = constantDefinitions.split("=")[1]

    return dictOfVars


def writeQuestion(question, dictVariables):
    # TODO Make this code work for multiple types of questions
    returnString = []

    # Remove the hidden constant definitions (between '{' and '}')
    # from the output questions
    if len(question.split("{")) > 1:
        question = question.split("{")[0] + question.split("}")[1]

    # Separate question by words
    file_read = question.split(" ")
    for value in file_read:
        # If word does not begin with a $, it is not a variable
        # append it normally
        if value[0] != "$":
            returnString.append(value)
        else:
            # Check if any key in the dictionary matches whatever
            # is after the $, and if so substitute the word with the
            # value in the dictionary by appending it to the question
            for i in dictVariables:
                if value[1::] == i:
                    returnString.append(dictVariables[i])

    return " ".join(str(x) for x in returnString)


def shuffleAnswers(answers):
    answerList = list(answers.items())
    shuffle(answerList)
    return(dict(answerList))


def writeAnswers(answers):
    returnString = []
    answers = shuffleAnswers(answers)
    print(answers)
    for i in answers:
        returnString.append(i)

    return "\n".join(str(x) for x in returnString)


def getQuestion(path):
    questionInput = readFile(path)
    print("readFile is equal to", questionInput)

    # This next line will use the code the user provides, it is currently
    # using the example addition class
    # Gives the variables dictionary to addition.generate,
    # which returns a tuple containing (filled dictionary of variables,
    # the correct answer to the question)
    varDict, answer = addition.generate(identifyVariables(questionInput))
    print("userChangeVariables is equal to", answer)
    pprint.pprint(varDict)

    question = writeQuestion(questionInput, varDict)
    answers = writeAnswers(answer)
    return question, answers


path = 'example1.txt'
question, answers = getQuestion('example1.txt')
print('\n')
print(question)
print(answers)
