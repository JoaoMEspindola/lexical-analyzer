import re
class RegexPatterns:
    def __init__(self) -> None:
        self.reservedWords = re.compile(r'int|float|char|bool|void|if|else|for|while|scanf|printf|main|return\b')
        self.operators = re.compile(r'=|\+|-|\*|\/|%|&&|\|\||!|>=|<=|>|<|!=|==\b')
        self.specialSymbols = re.compile(r'\(|\)|\{|\}|\[|\]|;|,|\.\b')

    def match_reserved_words(self, text):
        return self.reservedWords.findall(text)
    
    def match_operators(self, text):
        return self.operators.findall(text)
    
    def match_special_symbols(self, text):
        return self.specialSymbols.findall(text)
