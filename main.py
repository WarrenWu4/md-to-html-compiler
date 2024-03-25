from lexer import preprocess, tokenize 

def getFile(filename):
    lines = [] 
    try:
        with open(filename) as f:
           lines = f.readlines() 
    except Exception as e:
        exit(f"Error occurred reading file: {e}")
    return lines 

fLines = getFile("test-files/headings_test.md")
newLines = preprocess(fLines)

# print(newLines)


