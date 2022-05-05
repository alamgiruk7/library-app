import time

class Library:
    def __init__(self, listOfBooks) -> None:
        self.books = [i.lower() for i in listOfBooks]

    def displayAvailableBooks(self):
        print("\nBook Available right now:")
        for items in self.books:
            print(f"\t>> {items.title()}")
        print("\n\t\t\t\t\t<------------------------------------------------>")

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName.title()}. Kindly return it with in 30 days in original Condition.")
            self.books.remove(bookName)
        else:
            print(f"{bookName.title()} is not available right now. Please wait until the book is available.")
    
    def returnBook(self, bookName):
        print(f"Thank you for returning {bookName.title()}. Hope you have enjoyed reading it!")
        self.books.append(bookName)

    def donateBook(self):
        bookName = input("Please enter the name of the book you want to donate to the Central Library.\n")
        self.books.append(bookName)
        print(f"Thank you for donating {bookName.title()} to the Central Library!")



class Student:
    def returnBook(self):
        bookName = input("Enter the Book you want to return: ")
        return bookName.lower()

    def issueBook(self):
        bookName = input("Enter the Book you want to issue: ")
        return bookName.lower()





if __name__ == "__main__":

    print('''\n\n\t\t\t<------------------------- Welcome To Central library -------------------------> ''')

    centralLibrary = Library(["Alice in Wonderland", "Ali Baba & Fourty Thieves", "The Jungle Book", "Learn Python", "Learn Web Development"])
    student1 = Student()

    while(True):
        options = '''
        \t\t\t\t\t   1. Show available books
        \t\t\t\t\t   2. Issue a book
        \t\t\t\t\t   3. Return a book
        \t\t\t\t\t   4. Donate to the Library
        \t\t\t\t\t   5. Exit
        '''
        print(options)
        userInput = input("\t\t\t\t\t   Please choose an option: ")

        if userInput == "1":
            centralLibrary.displayAvailableBooks()

        elif userInput == "2":
            centralLibrary.borrowBook(student1.issueBook())

        elif userInput == "3":
            centralLibrary.returnBook(student1.returnBook())
        
        elif userInput == "4":
            centralLibrary.donateBook()

        elif userInput == "5":
            print("Thank You for choosing Central Library. Have a great day ahead!")
            time.sleep(3)
            exit()

        else:
            print("ouhhoo, You selected an invalid option.")

        
        