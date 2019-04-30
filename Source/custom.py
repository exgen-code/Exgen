import random


class custom:

    def __init__(self):
        pass

    @staticmethod
    def add(varDict):
        """ Returns the sum of the values with keys
        term1 and term2 in the dictionary
        """
        return varDict['term1'] + varDict['term2']

    @staticmethod
    def getAnswers(correctAnswer):
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
            deviation = random.randint(int(-(correctAnswer/4)),
                                       int(correctAnswer/4))
            if(deviation != 0):
                answers[correctAnswer + deviation] = False
        answers[correctAnswer] = True
        return(answers)

    @staticmethod
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

    @staticmethod
    def generate(varDict):
        """Fills the variable dictionary and generates the correct answer
        Returns a tuple containing the filled variable dictionary and the
        correct answer, respectively"""
        varDict = custom.generateNumbers(varDict)
        answer = custom.add(varDict)
        return(varDict, custom.getAnswers(answer))
