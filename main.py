import sys
from stats import get_num_words
from stats import num_times
from stats import sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    directory = sys.argv[1]
    book_text = get_book_text(directory)
    num_words = get_num_words(book_text)

    char_freq = num_times(book_text)
    
    sorted_chars = sort_list(char_freq)

    # print(f"{num_words} words found in the document")
    # print(char_freq)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {directory}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        this_char = char_dict["char"]
        if not this_char.isalpha():
            continue
        this_count = char_dict["num"]
        print(f"{this_char}: {this_count}")

    print("============= END ===============")


main()
