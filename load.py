# This is the categories of the csv file
# Book,Author(s),Original language,year of publication,Genre,Approximate sales

from Color import color

class Book:
    """
        Simple Book class
    """
    def __init__(self, Name:str, Authors:str, Original_language:str, year:str,Genre:str,Appoximated_sales:str) -> None:
        self.name:str = Name
        self.authors:str = Authors
        self.language:str = Original_language
        self.year:int = int(year)
        self.genre:str = Genre
        self.salses:str = Appoximated_sales
    
    @property
    def str(self) -> str:
        color
        result = f"{color.clear+color.bold+color.blue+self.name} :\n"
        result += f"\t{color.clear+color.blue}├──Author(s) :{color.white+color.italic} {self.authors}\n"
        result += f"\t{color.clear+color.blue}├──Original language :{color.white+color.italic} {self.language}\n"
        result += f"\t{color.clear+color.blue}├──Year of publication :{color.white+color.italic} {self.year}\n"
        result += f"\t{color.clear+color.blue}├──Genre :{color.white+color.italic} {self.genre}\n"
        result += f"\t{color.clear+color.blue}└──Approximate sales :{color.white+color.italic} {self.salses}"
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

