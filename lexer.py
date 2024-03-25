"""
todo:
    1. start tokenizer
"""

"""
removes irrelevant characters in text before tokenizing
"""
def preprocess(text):
    startIndex = 0
    endIndex = -1 
    while (text[startIndex] == "\n" or text[startIndex] == " "):
        startIndex += 1
    while (text[endIndex] == "\n" or text[endIndex] == " "):
        endIndex -= 1
    return text[startIndex:endIndex+1] 

"""
identifies special characters
"""
def tokenize(text):
    tokens = []
    currToken = ""
    for char in text:
        if (char == "\n"):
            storeToken(currToken, tokens)
            tokens.append("\n")
        elif (char == " " and currToken != ""):
            tokens.append(currToken)
            currToken = ""
        else:
            currToken += char

    return tokens

"""
helper function for tokenize
"""
def storeToken(currToken, tokens):
    if (currToken != ""):
        tokens.append(currToken)
        currToken = ""


    






