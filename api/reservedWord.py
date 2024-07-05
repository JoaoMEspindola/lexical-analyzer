class ReservedWord:
    def __init__(self, words) -> None:
        self.words = words

    def findReservedWord(self, word):
        if word in self.words:
            return True
        return False
    
    