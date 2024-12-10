class Library:
    book_list=[]

    def entry_book(self,book):
        self.book_list.append(book)


class Book(Library):
    def __init__(self, book_id, title,author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True

    def returnBookId(self):
        return self.__book_id

    def view_book_info(self):
        status = ""
        if self.__availability:
            status = "Available"
        else:
            status = "Not Available"
        print(f'ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {status}')
    
    def borrow_book(self, bookId):
        if self.__book_id == bookId:
            if self.__availability:
                self.__availability = False
                print(f"Book '{self.__title}' borrwed sucessfully.")
            else:
                print("Trying to borrow a book that is already borrowed.")
        else:
            print("Invalid book ID")

    def return_book(self, bookId):
        if self.__book_id == bookId:
            if self.__availability == False:
                self.__availability = True
                print(f"Book '{self.__title}' returned sucessfully.")
            else:
                print("Trying to return a book that is not borrowed")
        else:
            print("Invalid book ID")



def main():
    li = Library()
    li.entry_book(Book(101, "Python Programming", "Jone Doe"))
    li.entry_book(Book(102, "Data Science Essentials", "Jane Smith"))
    li.entry_book(Book(103, "Machine Learning", "Alan Turing"))
    li.entry_book(Book(104, "Artificial Intelligence", "Marvin Minsky"))
    li.entry_book(Book(105, "Deep Learning", "Yann LeCun"))
    li.entry_book(Book(106, "Natural Language Processing", "Christopher Manning"))
    li.entry_book(Book(107, "Statistics for Data Science", "David C. Hsu"))
    li.entry_book(Book(108, "Python for Data Analysis", "Wes McKinney"))

    while True:
        print("-----Welcome to the Library-----")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Return Book")
        print("")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Enter a valid input number!")
            print("")
            continue
        
        try:
            if choice == 1:
                print("Library bookss:")
                for book in Library.book_list:
                    book.view_book_info()
                print("")
            elif choice == 2:
                try:
                    bookId = int(input("Enter book ID to borrow: "))
                except:
                    print("please enter a valid integer Book ID!")
                    print("")
                    continue
                flg = True
                for book in Library.book_list:
                    if bookId == book.returnBookId():
                        book.borrow_book(bookId)
                        print("")
                        flg = False
                        break
                if flg:
                    print("Invalid book ID")
                    print("")

                       
                        
            elif choice == 3:
                try:
                    bookId = int(input("Enter book ID to return: "))
                except:
                    print("please enter a valid integer Book ID!")
                    print("")
                    continue
                flg = True
                for book in Library.book_list:
                    if bookId == book.returnBookId():
                        book.return_book(bookId)
                        print("")
                        flg = False
                        break
                if flg:
                    print("Invalid book ID")
                    print("")


            elif choice == 4:
                print("Exiting the Library System...")
                break
            else:
                print("Enter a valid choice number!") 
        except:
            print("Something Went wrong please try again!")

main()