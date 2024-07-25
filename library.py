class library:
    def __init__(self):
        self.books={
           'Wings of fire':5,
           'Rich Dad Poor Dad':7,
           'The Mocking Bird':10,
           '2 states_new':4,
           'do Epic shits':15
        }
        
    def display_available_books(self):
        for book,count in self.books.items():
            print(f'{book}:{count}')
            
    def add_book(self,book,count=1):
        
        if book in self.books and self.books[book]>0:
            self.books[book]+=count
        else:
            self.books[book]=count
        return self.books
    
    def borrow_book(self,book):
        if book in self.books and self.books[book]>0:
            self.books[book]-=1
        return self.books.get(book,0)
    
lib=library()
lib.display_available_books()

lib.add_book('Shyamchi aai')
lib.display_available_books()

lib.borrow_book('Wings of fire')
lib.display_available_books()


