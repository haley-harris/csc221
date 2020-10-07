import re

def strip_string(whitespace_str, character=''):

    whitespace_regex = re.compile(r'^\s\s+')

    stripped_str = whitespace_regex.sub(character, whitespace_str)

    print(stripped_str)

    return stripped_str

whitespace_sentence = '  all this whitespace     '
character = 'e'

strip_string(whitespace_sentence)




