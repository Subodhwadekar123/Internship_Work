 # #Here’s a mini-project idea based on the concept of logging, exception handling, and file management. This exercise will help students apply the concepts in a practical scenario while reinforcing their understanding.

# Mini-Project: Library Management System Log Tracker
# Problem Statement
# Create a program that simulates a library management system where users can:

# Borrow books.
# Return books.
# Check available books.
# The program should:

# Log all user actions (borrow, return, invalid inputs, etc.) and any exceptions into a log file.
# At the end of the program, the log file should be cleared and reset for the next session.

# TIPS:-
# Setup:

# Create a list of books available in the library (e.g., ["Harry Potter", "1984", "To Kill a Mockingbird"]).
# Use a dictionary to keep track of which books are borrowed (e.g., {"Harry Potter": False, "1984": True}).
# Menu:

# Present the user with a menu:
# View available books
# Borrow a book
# Return a book
# Exit
# Requirements for Each Action:

# View Books:
# Display all books and their availability.
# Borrow a Book:
# Check if the book is available. If yes, allow the user to borrow and log the action. If not, log an error.
# Return a Book:
# Check if the book is borrowed. If yes, mark it as returned and log the action. If not, log an error.
# Exit:
# Before exiting, clear the log file.
# Error Handling:

# Handle invalid inputs, such as selecting a book that doesn't exist or entering invalid menu options, and log these errors.
# Logging Format:


# books dictionary ->

# books = {
#         "Harry Potter": {
#             "author": "J.K. Rowling",
#             "genre": "Fantasy",
#             "year": 1997,
#             "borrowed": False
#         },
#         "1984": {
#             "author": "George Orwell",
#             "genre": "Dystopian",
#             "year": 1949,
#             "borrowed": False
#         },
#         "To Kill a Mockingbird": {
#             "author": "Harper Lee",
#             "genre": "Fiction",
#             "year": 1960, 
#             "borrowed": False
#         }
#     }


from logging import *

def clearLogs():
    with open(r'C:\Users\subod\Internship 2024-25\Internship_Work\BookLogs.txt', 'w') as f:
        f.truncate(0)
    print("Log file is cleared...")

def configLogs():
    with open(r'C:\Users\subod\Internship 2024-25\Internship_Work\BookLogs.txt', 'a+') as f:
        pass
    basicConfig(filename=r'C:\Users\subod\Internship 2024-25\Internship_Work\BookLogs.txt',
                level=INFO,
                format='%(asctime)s - %(levelname)s - %(message)s')

clearLogs()
configLogs()

books = {
    "Harry Potter": {
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "year": 1997,
        "borrowed": False
    },
    "1984": {
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "borrowed": False
    },
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960,
        "borrowed": False
    }
}

def view_books():
    print("\nAvailable Books:\n")
    for book, BookValue in books.items():
        status = "Borrowed" if BookValue["borrowed"] else "Available"
        print(f"{book}:({BookValue['author']}, {BookValue['genre']}, {BookValue['year']}) - {status}")

def borrow_book(book_name):
    if book_name in books:
        if books[book_name]["borrowed"]:
            warning(f"Book '{book_name}' is already borrowed.")
            print(f"Book '{book_name}' is already borrowed.")
        else:
            books[book_name]["borrowed"] = True
            info(f"Book '{book_name}' has been borrowed.")
            print(f"Book '{book_name}' has been borrowed.")
    else:
        error(f"Book '{book_name}' does not exist.")
        print(f"Book '{book_name}' does not exist.")

def return_book(book_name):
    if book_name in books:
        if books[book_name]["borrowed"]:
            books[book_name]["borrowed"] = False
            info(f"Book '{book_name}' has been returned.")
            print(f"Book '{book_name}' has been returned.")
        else:
            warning(f"Book '{book_name}' was not borrowed.")
            print(f"Book '{book_name}' was not borrowed.")
    else:
        error(f"Book '{book_name}' does not exist.")
        print(f"Book '{book_name}' does not exist.")

def library_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_books()
            elif choice == 2:
                book_name = input("Enter the name of the book to borrow: ").strip()
                borrow_book(book_name)
            elif choice == 3:
                book_name = input("Enter the name of the book to return: ").strip()
                return_book(book_name)
            elif choice == 4:
                print("Exiting Library Management System. Goodbye!")
                break
            else:
                warning("Invalid choice. Please select a valid option.")
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            error("Invalid input. Please enter a number.")
            print("Invalid input. Please enter a number.")

library_menu()
