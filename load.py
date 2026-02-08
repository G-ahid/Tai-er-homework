# This is the categories of the csv file
# Book,Author(s),Original language,year of publication,Genre,Approximate sales

class Book:
    """
        Simple Book class
    """
    def __init__(self, Name:str, Authors:list[str], Original_language:str, year:str,Genre:str,Appoximated_sales:str) -> None:
        self.name:str = Name
        self.authors:list[str] = Authors
        self.language:str = Original_language
        self.year:int = int(year)
        self.genre:str = Genre
        self.salses:str = Appoximated_sales
    
    @property
    def str(self) -> str:
        result = f"{self.name} :\n"
        result += f"\t└──Author(s) : {self.authors}\n"
        result += f"\t└──Original language : {self.language}\n"
        result += f"\t└──Year of publication : {self.year}\n"
        result += f"\t└──Genre : {self.genre}\n"
        result += f"\t└──Approximate sales : {self.salses}"
        return result

    

def loadCSV(filename:str = "Books.csv") -> list[Book]:
    """
        Loads the csv file and return the list of Books
    """
    with open(filename) as f:
        # A list of books
        books:list[Book] = []
        # Gets each line an ignores the first one
        # As the first on has the categories not the data
        lines:list[str] = f.readlines()[1:]
        for line in lines:
            args = line.strip().split(',')
            for arg in args:
                arg = arg.strip()
            
            # We make a new Book and add it to the list of Books
            books.append(Book(
                args[0], # Name
                args[1], # Author(s)
                args[2], # Original Language
                args[3], # Year of Publication
                args[4], # Genre
                args[5]  # Approximate sales
            ))
        return books

if __name__ == "__main__":
    books = loadCSV()
    for book in books:
        print(book.name)
        print(book.authors, ' - ',end='')
        print(book.language, ' - ',end='')
        print(book.year, ' - ',end='')
        print(book.genre, ' - ',end='')
        print(book.salses, ' - ')
