def get_word_count(book_text):
    book = book_text.split()
    word_count = len(book)
    return word_count

def get_char_count(book_text):
    book = book_text.lower()
    char_count = {}
    for char in book:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count