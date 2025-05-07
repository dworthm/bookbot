from stats import get_num_words, get_num_chars, get_sorted_chars
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]
def main():
    num_words = get_num_words(filepath)
    chars = get_num_chars(filepath)
    sorted_chars = get_sorted_chars(chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in sorted_chars:
        if x["char"].isalpha():
            print(f"{x['char']}: {x['num']}")

main()
