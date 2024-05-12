from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C
tokens = tokenizer_obj.tokenize("国家公務員", mode)
for token in tokens:
    print(token.surface(), token.reading_form(), token.part_of_speech())
# Compare this snippet from app.py: