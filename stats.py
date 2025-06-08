def get_num_words(book_text):
    return len(book_text.split())

def num_times(book_text):
    char_freq = dict()
    for char in book_text:
        char = char.lower()
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    return char_freq

def sort_list(char_freq):
    sorted_list = []
    
    for char in char_freq:
        char_dict = dict()
        char_dict["char"] = char
        char_dict["num"] = char_freq[char]
        sorted_list.append(char_dict)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def sort_on(dict):
    return dict["num"]
