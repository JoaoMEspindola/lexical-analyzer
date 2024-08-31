import re
class RegexPatterns:
    def __init__(self) -> None:
        self.reservedWords = re.compile(r'int|float|char|bool|void|if|else|for|while|scanf|printf|main|return|string\b')
        self.operators = re.compile(r'=|\+|-|\*|\/|%|&&|\|\||!|>=|<=|>|<|!=|==\b')
        self.specialSymbols = re.compile(r'"|\(|\)|\{|\}|\[|\]|;|,|\.\b')
        self.comments = re.compile(r'//.*\n')
        self.textConsts = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
        self.alphanums = re.compile(r'^[a-zA-Z0-9]$')

    def match_reserved_words(self, text):
        return self.reservedWords.fullmatch(text)
    
    def match_operators(self, text):
        return self.operators.fullmatch(text)
    
    def match_special_symbols(self, text):
        return self.specialSymbols.fullmatch(text)
    
    def match_comments(self, text):
        return self.comments.fullmatch(text)
    
    def match_text_consts(self, text):
        return self.textConsts.fullmatch(text)
    
    def match_alpha_nums(self, text):
        return self.alphanums.fullmatch(text)
