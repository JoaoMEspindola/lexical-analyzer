def readFullFile(fileName):
    with open(fileName, 'r') as textFile:
        content = textFile.read()
    
    return content

def readFileAndTokenizeWords(fileName):
    with open(fileName, 'r') as textFile:
        content = textFile.read().strip().split()
    
    return content