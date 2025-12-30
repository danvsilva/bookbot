from stats import get_num_words, count_letters, sort_on


def main():
    book_path = "books/frankenstein.txt"
    listed_dicts = []
    num_of_words = get_num_words(get_book_text(book_path))
    letters_dict = count_letters(get_book_text(book_path))
    for l, count in letters_dict.items():
        listed_dicts.append({"letter": l, "count": count})
    listed_dicts.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for i in listed_dicts:
        print(f"{i['letter']}: {i['count']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
