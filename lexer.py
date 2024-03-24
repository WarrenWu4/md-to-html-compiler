"""
first stage of compiler.
reads markdown file and breaks it down into tokens such as keywords, identifiers, and operators.
tokens are then passed on to next stage
"""

tokenTypes = [
        "heading",
        "line break",
        "word",
        "bold",
        "italic",
        "bold italic"
        ]

def getFile(filename):
    text = ""
    try:
        with open(filename) as f:
           text = f.read() 
    except Exception as e:
        exit(f"Error occurred reading file: {e}")
    return text

def tokenize(text):
    tokens = [] # new token after every space or new line
    curr_token = ""
    for c in text:
        if (c == " " or c == "\n"):
            tokens.append(curr_token)
            curr_token = ""
        else:
            curr_token += c
    # remove leading white spaces
    for c in tokens:
        if (c == ""):
            tokens.pop(0)
        else:
            break
    # remove trailing white spaces
    for c in reversed(tokens):
        if (c == ""):
            tokens.pop()
        else:
            break
    return tokens






