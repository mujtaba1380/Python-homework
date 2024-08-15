class Book:
    def __init__(self,title,author,pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_pages(self):
        return self.__pages
    def set_title(self,title):
        self.__title = title
    def set_author(self,author):
        self.__author = author
    def set_pages(self,pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("pages can be positive!")
    def public(self,):
        print(f"title: {self.__title}",f"\nauthor: {self.__author}",f"\npages: {self.__pages}")
book = Book("database","ali",200)
book.set_pages(170)
book.set_title("programming")
book.set_author("Mujtaba Sarwari")
book.public()