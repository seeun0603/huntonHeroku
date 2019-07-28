from django.db import models

# Create your models here
class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key = True )
    user_pw = models.CharField(max_length=50)
    email= models.EmailField(max_length=75)
    level = models.IntegerField(default =0)

    def __str__(self):
        return self.user_id