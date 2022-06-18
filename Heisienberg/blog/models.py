from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()
class Post(models.Model):
    title : models.CharField(max_length=200)
    text : models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    created_date : models.DateTimeField()
    published_date: models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title


