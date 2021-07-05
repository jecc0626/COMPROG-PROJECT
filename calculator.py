class Calculator:
    def __init__(self):
        pass

    def Evaluate(self, inp):
        try:
            return eval(inp)
        except:
            return "Error"
