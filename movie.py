class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = int(rating)

       

    def review(self):
        if self.rating >= 8:
            return f"{self.title} is highly recommended"
        
        elif self.rating >= 5 and self.rating  <= 7:
            return f"{self.title} is decent" 
        
        elif self.rating < 5:
            return f"Maybe skip {self.title}"
        
        else:
            return "oops!"
        
movie1 = Movie("Peaky blinders", "Drama , Crime",  9)
print(movie1.review())
        