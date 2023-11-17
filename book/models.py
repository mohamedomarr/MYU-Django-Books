from django.db import models




RATING_STARS = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    biography = models.TextField(max_length=350)
    
    def __str__(self):
        return self.name

        
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    title = models.TextField(max_length=100)
    publication_date = models.DateField()
    price = models.CharField(max_length=25)
    genre = models.TextField(max_length=50)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_book')
    reviewer_name = models.CharField(max_length=150)
    content = models.TextField(max_length=1000)
    rating = models.CharField(choices=RATING_STARS, max_length=5)

    def __str__(self):
        return self.reviewer_name