class LogicalOperator:
    def __init__(self, operators) -> None:
        self.operators = operators

    def findLogicalOperator(self, operator):
        if operator in self.operators:
            return True
        return False