class library:
    def __init__(self,books):
        self.books=books
    def list_of_books(self):
        print("available books")
        for book in self.books:
            print(book)
    def borrow_books(self,borrow_books):
        if borrow_books in self.books:
            print("yes available.get your book now")
            self.books.remove(borrow_books)
        else:
            print("sorry,this book is not avaialable")
    def return_books(self,return_books):
        if return_books in self.books:
            print("you have return the book")
        else:
            print("enter the book name correctly")
        self.books.append(return_books)
books=['c','c++','java','javascript','python']
o1=library(books)
msg= """
1.available books
2.borrow books
3.return books
"""
while True:
    print(msg)
    ch=int(input("enter a number:"))
    if ch==1:
        o1.list_of_books()
    elif ch==2:
        books=input("enter a book name to borrow:")
        o1.borrow_books(books)
    elif ch==3:
        books=input("enter a book name to return:")
        o1.return_books(books)
    else:
        print("thank you come again")
        quit()
        
