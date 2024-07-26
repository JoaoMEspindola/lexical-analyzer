import dataReader
import regexPatterns
import displayData
import re

def treatComment(code, initialIndex):
    commentLine = code[initialIndex:]

    onlyCommentLine = ''
    for i in commentLine:
        if i != '\n':
            onlyCommentLine = onlyCommentLine + i
        else:
            break 

    finalIndex = initialIndex + len(onlyCommentLine)
    return onlyCommentLine, finalIndex

def isUnaccepted(token):
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token) == None:
        return False

    return True

def isAcceptedVariable(token, patterns, list_tokens):
    if patterns.match_reserved_words(list_tokens[-1]) and token[0].isdigit():
        print("Error: Variable starting with a digit.")
        return False

    if patterns.match_reserved_words(list_tokens[-1]) == True and isUnaccepted(token):
        print(patterns.match_reserved_words(list_tokens[-1]) == True)
        print(isUnaccepted(token))
        print("Error: Variable has unaccepted char.")
        return False
    
    return True
    

patterns = regexPatterns.RegexPatterns()
code = dataReader.readFullFile("../assets/test.txt")
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
                        break
                    else: 
                        id += 1
                        if not token in symbol_table:
                            symbol_table[token] = id
                        else:
                            id -= 1

                        list_tokens.append(f"'id': {symbol_table[token]}")
                token = ''
            if patterns.match_operators(c) or patterns.match_special_symbols(c):
                list_tokens.append(c)
    else:
        diff -= 1

    index += 1

if token:
    list_tokens.append(token)

displayData.displayResult(list_tokens, symbol_table)