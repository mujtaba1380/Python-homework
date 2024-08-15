class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
    def add_book(self,book_name):
        self.books.append(book_name)
    def remove_book(self,book_name):
        self.books.remove(book_name)
    def show_books(self):
        return self.books
lib = Library("Omid Library")
lib.add_book("database")
lib.add_book("programmig")
lib.add_book("nezame eteqady islam")
lib.add_book("searat alnabi")
lib.add_book("descrete mathematic")
lib.add_book("tarikh maaser")
lib.remove_book("tarikh maaser")
print(lib.show_books())