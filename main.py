from load import loadCSV, Book
from funcs import toInt, removeDuplicates, sort
from random import randint
from Color import color

menu:str = f"""
{color.italic+color.bold}Menu:
  └──{color.green}1.{color.white+color.italic+color.bold} Explore the content of the file
  └──{color.green}2.{color.white+color.italic+color.bold} View the different book genres in the file
  └──{color.green}3.{color.white+color.italic+color.bold} Sort the books by language
  └──{color.green}4.{color.white+color.italic+color.bold} Find the latest published book
  └──{color.green}5.{color.white+color.italic+color.bold} Get information about a book
  └──{color.green}6.{color.white+color.italic+color.bold} Random book
  └──{color.green}7.{color.white+color.italic+color.bold} Quit
"""

def main() -> None:
    # Fist message
    print("Welcome to the library of the Books\nWe have a library of the most sold books ever",end='')
    books: list[Book] = loadCSV() # We load the file
    # Main loop
    while True:
        print(menu,end='') 
        c:str = toInt(input()) # Get the user's choice as a number
        if c is None:
            print(color.red,color.bold,"Invalid option",color.clear)
            continue

        match c:
            case 1: # Explore the content of the file
                print(color.yellow,color.bold,"Listing all books...\n",color.clear)
                for book in books:
                    print(book.str)
            case 2: # View the different book genres in the file
                genres:list[str] = removeDuplicates([book.genre for book in books])
                genres_str:str = ""
                for genre in genres:
                    genres_str += genre.strip() + ", "

                print(color.yellow,"available genres are : ",color.clear,genres_str)

                c = input(color.bold,"\nWanted genre : ",color.clear)
                books_indecies = sort([book.genre for book in books], c)
                if not books_indecies:
                    print("No books found.")
                    continue
                print(color.yellow,color.bold ,f"Books found ({len(books_indecies)}) : ",color.clear)
                for i in books_indecies:
                    print(books[i].str)
            
            case 3: # Sort the books by language
                c = input(color.italic,"Language : ",color.clear)
                books_indecies = sort([book.language for book in books], c)
                if not books_indecies:
                    print(color.yellow,"No books found.",color.clear)
                    continue
                print(color.yellow,f"Books founds ({len(books_indecies)})",color.clear)
                for i in books_indecies:
                    print(books[i].str)

            case 4: # Find the latest published book
                newest = books[0]
                for book in books:
                    if book.year > newest.year:
                        newest = book

                print(color.yellow,"The newest book is : ",color.clear)
                print(newest.str)

            case 5: # Get information about a book 
                c = input(color.bold,"Search : ",color.clear)
                books_indecies = sort([book.name for book in books], c)
                if not books_indecies:
                    print(color.yellow,"No books found with that name.",color.clear)
                    continue
                _books = [books[i] for i in books_indecies]
                if len(_books) == 1:
                    print(color.yellow,"Book found :",color.clear)
                    print(_books[0].str)
                    continue

                for i,book in enumerate(_books):
                    print(i+1,'. ',book.name)
                while True:
                    c = toInt(input(color.yellow,f"Found {len(_books)}, which one do you want : "),color.clear)
                    if c is None or c < 1 or c > len(_books):
                        print(color.bold,color.red,"Invalid choice, try again.",color.clear)
                        continue
                    
                    print(_books[c - 1].str)
                    break

            case 6: # Random book
                print(books[randint(0, len(books)) - 1].str)

            case 7: # Quit
                print(color.magenta,color.bold,color.italic,"\nThank you for using my program !")
                return

                    

if __name__ == "__main__":
    main()