from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_id = models.IntegerField()  # stores user_id from Flask service
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title