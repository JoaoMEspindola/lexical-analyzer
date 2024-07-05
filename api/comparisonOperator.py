class ComparisonOperator:
    def __init__(self, operators) -> None:
        self.operators = operators

    def findComparisonOperator(self, operator):
        if operator in self.operators:
            return True
        return False