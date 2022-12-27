from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="ebook/images/")
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE)
    readAgain = models.BooleanField()

    def __str__(self) -> str:
        return self.text
