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
        
        