def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    # convert char_dict to a list of dicts before sort it
    chars_list = [{"char": k, "count": v} for k, v in chars_dict.items()]

    chars_list.sort(reverse=True, key=sort_on)

    print(f"--- Report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for c in chars_list:
        print(f"The {c['char']} character was found {c['count']} times")
    print(f"--- End Report ---")


def sort_on(dict):
    return dict["count"]


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()
