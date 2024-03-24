from lexer import getFile, tokenize 

text = getFile("test-files/headings_test.md")
tokens = tokenize(text)

print(tokens)


