class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"The book {book1.title} is authored by {book1.author}."

book1 = book("Gifted Hands", "Ben Carson")

print(book1.describe())
