def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = list(chars_dict.items())
    chars_list.sort()
    print(chars_list)
    pretty_print(book_path, chars_list, num_words)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars and lowered.isalpha(): # letter (lowered) is in chars, increment it
            chars[lowered] += 1
        elif lowered.isalpha():                    # if not set to one
            chars[lowered] = 1
    return chars

def get_character_sums(text):
    words = text.split()
    return len(words)

def pretty_print(book_path, chars_list, num_words):
    print(f"--- Begin report of {book_path} ---" )
    print(f"{num_words} words found in the document\n")
    for key, value in chars_list:
        print(f"The {key} character was found {value} times")
    print("--- End report ---")
    
main()
