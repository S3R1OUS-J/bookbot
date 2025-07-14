import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

from stats import num_of_words

from stats import chr_count

from stats import sorted_list

def main():
    if len(sys.argv) == 2:
        book = sys.argv[1]
        file_contents = get_book_text(book)
        num_words = num_of_words(file_contents)
        num_message = f"Found {num_words} total words"
        counts = chr_count(file_contents)
        list_of_chr = sorted_list(counts)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(num_message)
        print("--------- Character Count -------")
        for item in list_of_chr:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
