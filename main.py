import sys
from stats import count_words, char_counter, sorted_char_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    chars_counted = char_counter(text)
    opop = sorted_char_dict(chars_counted)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for temp_char in opop:
        if temp_char[0]["char"].isalpha():
            print(f"{temp_char[0]["char"]}: {temp_char[1]["num"]}")
    print("============= END ===============")

    

main()