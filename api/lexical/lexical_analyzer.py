import dataReader
from lexical import regexPatterns
from lexical import displayData
import re

def lexical_analysis(file):
    try:
        def treatComment(code, initialIndex):
            commentLine = code[initialIndex:]

            onlyCommentLine = ''
            for i in commentLine:
                if i != '\n':
                    onlyCommentLine += i
                else:
                    break 

            finalIndex = initialIndex + len(onlyCommentLine)
            return onlyCommentLine, finalIndex

        def isUnaccepted(token):
            return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token) is not None

        def isAcceptedVariable(token, patterns, list_tokens):
            if patterns.match_reserved_words(list_tokens[-1]) and token[0].isdigit():
                print("Error: Variable starting with a digit.")
                return False

            if patterns.match_reserved_words(list_tokens[-1]) and not isUnaccepted(token):
                print("Error: Variable has unaccepted char.")
                return False
            
            return True

        patterns = regexPatterns.RegexPatterns()
        code = dataReader.readFullFile(file)
        token = ''
        list_tokens = []
        symbol_table = {}
        id = 0
        last_char = ''
        index = 0
        foundComment = False
        diff = 0

        for c in code:
            if c == '/' and last_char == '/':
                onlyCommentLine, finalIndex = treatComment(code, index + 1)
                foundComment = True
                diff = finalIndex - index
                last_char = ''
                list_tokens[-1] = "//"
                list_tokens.append(onlyCommentLine)
            
            last_char = c
            
            if diff == 0:
                if patterns.match_alpha_nums(c):
                    token += c
                else:
                    if token:
                        if patterns.match_reserved_words(token):
                            list_tokens.append(token)    
                        else:
                            if not isAcceptedVariable(token, patterns, list_tokens):
                                return False
                            else: 
                                id += 1
                                if token not in symbol_table:
                                    symbol_table[token] = id
                                else:
                                    id -= 1

                                list_tokens.append('id')
                        token = ''
                    if patterns.match_operators(c) or patterns.match_special_symbols(c):
                        list_tokens.append(c)
            else:
                diff -= 1

            index += 1

        if token:
            list_tokens.append(token)

        displayData.displayResult(list_tokens, symbol_table)
        return list_tokens

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
