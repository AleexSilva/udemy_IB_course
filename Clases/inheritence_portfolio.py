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
        self.availablety = True
        
    def borrow(self):
        """
        Mark the book as borrowed if there is available
        """
        if self.availablety:
            self.availablety = False
            print(f'{self.title} have been borrowed')
        else:
            print(f'Sorry, but {self.title} is not available')
    
    def returns (self):
        """
        Mark the book as available for loan
        """
        self.availablety = True
        print(f'{self.title} have been returned')
        