# Library Management system.
class Book:
    pass
class Library(Book):
    pass

bookObj=Book()
libraryObj=Library()
while True:
    choice=int(input("Enter\n1.To add book\n2.To search book\n3.To remove book\n4.To exit"))
    if choice==4:
        print("Exiting ...")
        break
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case _:
            print("Invalid choice")
    