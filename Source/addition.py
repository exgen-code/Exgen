import random


class addition:

    def __init__(self):
        pass

    def add(varDict):
        """ Returns the sum of the values with keys
        term1 and term2 in the dictionary
        """
        return varDict['term1'] + varDict['term2']

    def getAnswers(n):
        """ Creates a dictionary for the answers and generates wrong
        answers that are the right answer plus a random number
        between (-)25% of the right answer and 25% of the right answer
        This will loop until 4 distinct wrong answers are generated
        The answers will be keys that have boolean elements based on whether
        they are correct or incorrect (true or false)
        Returns a dictionary of answers
        """
        answers = {}
        while(len(answers) < 4):
            deviation = random.randint(int(-(n/4)), int(n/4))
            if(deviation != 0):
                answers[n + deviation] = False
        answers[n] = True
        return(answers)

    def generateNumbers(varDict):
        """Generates random numbers (bounded by minbound and maxbound)
        for every key without a value in the variable dictionary
        Returns the modified variable dictionary
        """
        for i in varDict:
            if (varDict[i] == ""):
                if ('minbound' in varDict and 'maxbound' in varDict):
                    varDict[i] = random.randint(int(varDict['minbound']),
                                                int(varDict['maxbound']))
                if ('minbound' in varDict and 'maxbound' not in varDict):
                    varDict[i] = random.randint(int(varDict['minbound']),
                                                50)
                if ('minbound' not in varDict and 'maxbound' in varDict):
                    varDict[i] = random.randint(10,
                                                int(varDict['maxbound']))
                if ('minbound' not in varDict and 'maxbound' not in varDict):
                    varDict[i] = random.randint(10,
                                                50)
        return varDict

    def generate(varDict):
        """Fills the variable dictionary and generates the correct answer
        Returns a tuple containing the filled variable dictionary and the
        correct answer, respectively"""
        varDict = addition.generateNumbers(varDict)
        answer = addition.add(varDict)
        return(varDict, addition.getAnswers(answer))
