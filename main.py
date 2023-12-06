import os

def main():
    books_path = "books/"
    list_of_books = book_list(books_path)
    
    print(f"Processing library at path: {books_path}")
    for book in list_of_books:
        words = book_word_count(books_path, book)
        chars = book_letter_count(books_path, book)
        unsorted_chars = []
        print(f"Scanning book {book}")
        print(f"Found {words} words in the document {book}")
        print("")
        for c in chars:
            if c.isalpha():
                unsorted_chars.append((c,chars[c]))
        unsorted_chars.sort(key=lambda char: char[1], reverse=True)
        for pair in unsorted_chars:
            print(f"The '{pair[0]}' character was found {pair[1]} in the document")


def book_list(books_path):
    list_of_books = []
    books = os.listdir(books_path)
    for book in books:
        list_of_books.append(book)
    return list_of_books

def book_as_string(books_path, book_title):
    book_text = ""
    with open(books_path + book_title) as book:
        book_text = book.read()
    return book_text

def book_word_count(books_path, book_title):
    words = book_as_string(books_path, book_title).split()
    return(len(words))

def book_letter_count(books_path, book_title):
    text_as_string = book_as_string(books_path, book_title).lower()
    character_count = {}
    character_list = []

    for c in text_as_string:
        if c in character_count:
            character_count[c] +=1
        else:
            character_count[c] = 1
    
    return character_count

main()
        
"""
COUNT WORDS
Add a new function to your script that takes the text from the book as a string, and returns the number of words.

Add a print() statement, then run your code to make sure it's doing what you expect. For the Frankenstein book, you should get 77986 words!
"""

"""
COUNT LETTERS
Add a new function to your script that takes the text from the book as a string, and returns the number of times each character appears in the string. Convert any uppercase letters to lowercase letters, we don't want duplicates.

HINTS
I'd recommend using a dictionary of String -> Integer.

When you print out the dictionary it should look something like this:

{'p': 6121, 'r': 20818, 'o': 25225, ...
"""