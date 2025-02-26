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

def sort_on(dict):
    return dict["count"]

def char_count_to_sorted_list(char_count):
    sorted_list = []
    for key, value in char_count.items():
        sorted_list.append({"char": key, "count": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list