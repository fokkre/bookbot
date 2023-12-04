import os

def main():
    books_path = "books/"
    list_of_books = book_list(books_path)
    
    for book in list_of_books:
        #print(book_as_string(books_path, book))
        print(book_word_count(books_path, book))
        #print(book_letter_count(books_path, book))

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

#def book_letter_count():

    # with open("books/frankenstein.txt") as b:
    #     book_as_string = ""
    #     character_count = {}

    #     book_as_string = b.read().lower()
    #     for c in book_as_string:
    #         if c in character_count:
    #             character_count[c] +=1
    #         else:
    #             character_count[c] = 0
        
    #     print(character_count)

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