from django.db import models

# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="ebook/images/")
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title
