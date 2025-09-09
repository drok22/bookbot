from sys import argv, exit
from stats import get_chars_dict, get_num_words, get_counts_list


def get_book_text(path: str) -> str:
    file_contents = None

    with open(path) as f:
        file_contents = f.read()

    return file_contents


def main():
    path = None

    print(argv)

    if len(argv) == 2:
        path = argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    text = get_book_text(path)
    num_words = get_num_words(text)
    chars = get_chars_dict(text)
    counts = get_counts_list(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in counts:
        if str.isalpha(dict['char']):
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


if __name__ == '__main__':
    main()
