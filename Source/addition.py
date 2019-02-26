import random


class addition:

    def __init__(self):
        pass

    def add(varDict):
        return varDict['term1'] + varDict['term2']

    def generateNumbers(varDict):
        for i in varDict:
            if (varDict[i] == ""):
                varDict[i] = random.randint(int(varDict['minbound']),
                                            int(varDict['maxbound']))
        return varDict

    def generate(varDict):
        varDict = addition.generateNumbers(varDict)
        return(varDict, addition.add(varDict))
