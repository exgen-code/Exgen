import random
class addition:

    def __init__(self):
        pass

    def add(self,varDict):
       return varDict['Y'] + varDict['X']
    def generateNumbers(self,varDict):
        for i in varDict:
            if (varDict[i] == ""):
                varDict[i] = random.randint(int(varDict['minbound']), int(varDict['maxbound']))
        return varDict
    def generate(self,varDict):
        varDict = self.generateNumbers(varDict)
        return(varDict,self.add(varDict))

