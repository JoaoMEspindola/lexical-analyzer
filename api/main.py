import dataReader
import regexPatterns

patterns = regexPatterns.RegexPatterns()
code = dataReader.readFullFile("./assets/test.txt")


print("Palavras Reservadas: ", patterns.match_reserved_words(code))
print("Operadores: ", patterns.match_operators(code))
print("Símbolos Especiais: ", patterns.match_special_symbols(code))
print("Comentários: ", patterns.match_comments(code))
print("Constantes de texto: ", patterns.match_text_consts(code))