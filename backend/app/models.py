from django.db import models

# Create your models here.

#books table with fields bookId, bookName, author, price and isbn.
class Books(models.Model):
    bookId = models.IntegerField()
    bookName = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    isbn = models.IntegerField()
    
    def __str__(self):
        return self.title