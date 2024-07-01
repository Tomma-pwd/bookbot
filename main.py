import string
def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    word_count = 0
    in_word = False
    
    for char in text:
        if char.isspace():
            if in_word:
                word_count += 1
                in_word = False
        else:
            in_word = True
    
    if in_word:
        word_count += 1
    
    return word_count

def get_char_count(text):
    char_counter = {char:0 for char in string.printable}
    char_count = {}
    for char in text:
        char_counter[char.lower()] += 1
    for k, v in char_counter.items():
        if v != 0:
            char_count[k] = v
    return char_count

def main():
    book_path = "books/frankenstein.txt"
    text = read_file(book_path)
    print(f"---Report for the {book_path}")
    print(f"Number of words: {get_num_words(text)}")
    for k, v in get_char_count(text).items():
        print(f"{k} : {v}")
    pass

main()