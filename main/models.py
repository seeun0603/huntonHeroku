from django.db import models

# Create your models here.
class Book(models.Model):
    bookName = models.CharField(max_length=50)
    author = models.CharField(max_length =50)
    publisher = models.CharField(max_length =50)
    kdc = models.IntegerField()
    img = models.ImageField(upload_to = 'images/', null=True, blank=True)

    def __str__(self):
        return self.bookName

class Keyword(models.Model):
    key_name = models.CharField(max_length=1000)
    book_id = models.ForeignKey(Book, db_column='Book.id', on_delete=models.CASCADE)

    def _str__(self):
        return self.id