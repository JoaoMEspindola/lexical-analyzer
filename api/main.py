import dataReader
import reservedWord
import arithmeticOperator
import comparisonOperator
import logicalOperator
import specialSymbol

reservedWords = reservedWord.ReservedWord(dataReader.readFileAndTokenizeWords("./assets/reservedWords.txt"))
arithmeticOperators = arithmeticOperator.ArithmeticOperator(dataReader.readFileAndTokenizeWords("./assets/arithmeticOperators.txt"))
comparisonOperators = comparisonOperator.ComparisonOperator(dataReader.readFileAndTokenizeWords("./assets/comparisonOperators.txt"))
logicalOperators = logicalOperator.LogicalOperator(dataReader.readFileAndTokenizeWords("./assets/logicalOperators.txt"))
specialSymbols = specialSymbol.SpecialSymbol(dataReader.readFileAndTokenizeWords("./assets/specialSymbols.txt"))