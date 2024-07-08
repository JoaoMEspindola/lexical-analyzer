import dataReader
import regexPatterns

patterns = regexPatterns.RegexPatterns()
code = dataReader.readFullFile("./assets/test.txt")
token = ''
list_tokens = []
symbol_table = []
id = 0

for c in code:
    if patterns.match_alpha_nums(c):
        token += c
    else:
        if token:
            if patterns.match_reserved_words(token):
                list_tokens.append(token)    
            else:
                id += 1
                list_tokens.append({'id': id})
                symbol_table.append({id: token})
            token = ''
        if patterns.match_operators(c) or patterns.match_special_symbols(c):
            list_tokens.append(c)

if token:
    list_tokens.append(token)

print(f'Lista de tokens: {list_tokens}')
print(f'Tabela de símbolos: {symbol_table}')