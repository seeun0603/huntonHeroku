from django.db import models
from main.models import Book
from signup.models import User

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length= 100)
    bookName = models.ForeignKey(Book, db_column = 'Book.id', on_delete=models.CASCADE)
    author = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now = True)
    lookup = models.IntegerField(default=0)
    context = models.TextField()

    def __str__(self):
        return self.title

class Like(models.Model):
    user_id = models.ForeignKey(User, db_column = 'User.user_id', on_delete = models.CASCADE)
    board_id = models.ForeignKey(Board, db_column = 'Board.id', on_delete = models.CASCADE)
    count = models.IntegerField(default=0)

class Comment(models.Model):
    user_id = models.ForeignKey(User, db_column='User.user_id', on_delete=models.CASCADE) 
    board = models.ForeignKey(Board, on_delete = models.CASCADE, related_name='comments')
    contents = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.contents