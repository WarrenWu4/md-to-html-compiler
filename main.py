from lexer import preprocess, tokenize 

def getFile(filename):
    text = "" 
    try:
        with open(filename) as f:
            text = f.read()
    except Exception as e:
        exit(f"Error occurred reading file: {e}")
    return text 

text = getFile("test-files/headings_test.md")
preprocessedText = preprocess(text)
tokens = tokenize(preprocessedText)

print([preprocessedText])
print(tokens)


