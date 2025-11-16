from stats import *
import sys

class Pipe:
    def __init__(self, value):
        self.value = value

    def __or__(self, func):
        self.value = func(self.value)
        return self

    def result(self):
        return self.value


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    sorted_char_num_dict = (
        Pipe(book_text)
        | get_each_char_count
        | format_to_char_num_dict
        | sort_by_num_counts
    ).result()

    for a in sorted_char_num_dict:
        print(f"{a["char"]}: {a["num"]}")

    print("============= END ===============")

def format_to_char_num_dict(dict):
    result = []
    for char, num in dict.items():
        result.append({"char": char,"num": num})
    return result

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()