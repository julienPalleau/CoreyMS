import re

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'^S')
matches = pattern.finditer(sentence)

for match in matches:
    print(match)
