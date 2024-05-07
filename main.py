def main():
    book_dir = 'books/frankenstein.txt'
    book_text = book_parse(book_dir)
    ltr_count = sorted_letters_count(letters_count(book_text))
    print(f'--- Begin report of {book_dir} ---')
    print('Number of words:', words_count(book_text))
    for n in ltr_count:
        print(f'The {n} character was found {ltr_count[n]} times')
    print('--- End report ---')


def words_count(text):
    return len(text.split())


def letters_count(text):
    letters_dict = {}
    for n in text.lower():
        if n in 'abcdefghijklmnopqrstuvwxyz':
            if n not in letters_dict:
                letters_dict[n] = 1
            else:
                letters_dict[n] += 1
    return letters_dict


def sorted_letters_count(letters_dict):
    sorted_dict = {}
    for n in sorted(letters_dict, key=letters_dict.get, reverse=True):
        sorted_dict[n] = letters_dict[n]
    return sorted_dict


def book_parse(path):
    with open(path) as book:
        return book.read()


if __name__ == '__main__':
    main()
