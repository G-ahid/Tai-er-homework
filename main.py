import enum
from funcs import sort
from load import Book
from load import loadCSV
from funcs import toInt, removeDuplicates
menu:str = """
Menu:
  └──1. Explore the content of the file
  └──2. View the different book genres in the file
  └──3. Sort the books by language
  └──4. Find the latest published book
  └──5. Get information about a book
  └──6. Quit
"""

def main() -> None:
    print("Welcome to the library of the Books\nWe have a library of the most sold books ever",end='')
    books: list[Book] = loadCSV()

    while True:
        print(menu)
        c:str = toInt(input())
        if c is None:
            print("Invalid option")
            continue

        match c:
            case 1:
                print("Listing all books...\n")
                for book in books:
                    print(book.str)
            case 2:
                genres:list[str] = removeDuplicates([book.genre for book in books])
                genres_str:str = ""
                for genre in genres:
                    genres_str += genre.strip() + ", "

                print(f"available genres are : f{genres_str}")

                c = input("\nWanted genre : ")
                books_indecies = sort([book.genre for book in books], c)
                if not books_indecies:
                    print("No books found.")
                    continue
                print(f"Books founds ({len(books_indecies)})")
                for i in books_indecies:
                    print(books[i].str)
            
            case 3:
                c = input("Language : ")
                books_indecies = sort([book.language for book in books], c)
                if not books_indecies:
                    print("No books found.")
                    continue
                print(f"Books founds ({len(books_indecies)})")
                for i in books_indecies:
                    print(books[i].str)

            case 4:
                newest = books[0]
                for book in books:
                    if book.year > olders.year:
                        newest = book

                print("The newest book is : ")
                print(newest.str)

            case 5:
                c = input("Search : ")
                books_indecies = sort([book.name for book in books], c)
                if not books_indecies:
                    print("No books found with that name.")
                    continue
                _books = [books[i] for i in books_indecies]
                if len(_books) == 1:
                    print("Book found :")
                    print(_books[0].str)
                    continue

                for i,book in enumerate(_books):
                    print(i+1,'. ',book.name)
                while True:
                    c = toInt(input(f"Found {len(_books)}, which one do you want : "))
                    if c is None or c < 1 or c > len(_books):
                        print("Invalid choice, try again.")
                        continue
                    
                    print(_books[c - 1].str)
                    break

            case 6:
                print("\nThank you for using my program !")
                return

                    

if __name__ == "__main__":
    main()