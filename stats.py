from operator import itemgetter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(filepath):
    contents = get_book_text(filepath)
    words = contents.split()
    return len(words)

def get_num_chars(filepath):
    contents = get_book_text(filepath)
    chars = {}
    for char in contents:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars

def get_sorted_chars(chars):
    sorted_chars = []
    for char in chars:
        char_pair = {}
        char_pair["char"] = char
        char_pair["num"] = chars[char]
        sorted_chars.append(char_pair)
    sorted_chars.sort(key=itemgetter("num"), reverse=True)
    return sorted_chars
