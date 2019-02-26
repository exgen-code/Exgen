import random


class addition:

    def __init__(self):
        pass

    def add(varDict):
        """ Returns the sum of the values with keys
        term1 and term2 in the dictionary
        """
        return varDict['term1'] + varDict['term2']

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
                    varDict[i] = random.randint(1,
                                                int(varDict['maxbound']))
                if ('minbound' not in varDict and 'maxbound' not in varDict):
                    varDict[i] = random.randint(1,
                                                50)
        return varDict

    def generate(varDict):
        """Fills the variable dictionary and generates the correct answer
        Returns a tuple containing the filled variable dictionary and the
        correct answer, respectively"""
        varDict = addition.generateNumbers(varDict)
        return(varDict, addition.add(varDict))
