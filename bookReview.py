class BookReview:

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = int(rating)

    def summary(self):
        if self.rating >= 9 and self.rating <= 10:
            return f"{self.title} is a Must-Read book"
        
        elif self.rating >= 6 and self.rating <= 8:
            return f"{self.title} is Worth a look"
        
        elif self.rating < 6:
            return f"{self.title} is Not recommended"
        
        else:
            "Oops!"
        
book1 = BookReview("Gifted Hands", "Ben Carson", 10)
print(book1.summary())