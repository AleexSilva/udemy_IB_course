class Book:
    """
    Class that represent a generic book
    """    
    
    def __init__(self,title,author):
        """
        Constructor
        """
        self.title = title
        self.author = author
        self.availability = True
        
    def borrow(self):
        """
        Mark the book as borrowed if there is available
        """
        if self.availability:
            self.availability = False
            print(f'{self.title} have been borrowed')
        else:
            print(f'Sorry, but {self.title} is not available')
    
    def returns (self):
        """
        Mark the book as available for loan
        """
        self.availability = True
        print(f'{self.title} have been returned')
        
# Create a class for users

class Users:
    """
    Retpresent an individual who request or retun a book.
    """
    
    def __init__(self,user):
        """
        User Constructor
        """
        self.user = user
    
    def request_loan(self,book):
        """
        Method to request a book from the system
        """
        print(f'{self.user} request the book {book.title}')
        book.borrow()
    
    def retun_book(self,book):
        """
        Return a book which was requested
        """
        print(f'{self.user} has returned the book {book.title}. NOw is available for loan')
        book.returns()

# Class to combine all functionalities from users and books

class LibrarySystem(Book,Users):
        """
        Class that represent a library system
        """
        def __init__(self,title,author,user):
            Book.__init__(self,title=title,author=author)
            Users.__init__(self,user=user)
        
        def manage_loan(self):
            """
            request a book loan 
            """
            self.request_loan(self)
        
        def manage_return(self):
            """
            Return a book that have had borrowed
            """
            self.retun_book(self)
            

