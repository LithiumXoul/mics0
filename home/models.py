from django.db import models

class Writter(models.Model):
    name = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    poster = models.ForeignKey(Writter, null=True, on_delete = models.SET_NULL)
    title = models.CharField(max_length=100,default = "My post")
    body = models.TextField()

    def __str__(self):
        return self.title
