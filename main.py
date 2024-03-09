def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_of_letters = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for key, value in count_of_letters.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    counts = {}
    for letter in alphabet:
        counts[letter] = text.count(letter)
    return counts


main()
