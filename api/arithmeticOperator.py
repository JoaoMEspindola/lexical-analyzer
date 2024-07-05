class ArithmeticOperator:
    def __init__(self, operators) -> None:
        self.operators = operators

    def findArithmeticOperator(self, operator):
        if operator in self.operators:
            return True
        return False