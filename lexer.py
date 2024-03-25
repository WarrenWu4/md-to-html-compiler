"""
todo:
    1. start tokenizer
"""

"""
removes irrelevant characters in text before tokenizing
"""
def preprocess(lines):
    while (lines[0].strip(" ") == "\n"):
        lines.pop(0)
    while (lines[-1].strip(" ") == "\n"):
        lines.pop()
    return lines   

def tokenize(lines):
    pass






