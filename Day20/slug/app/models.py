from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.IntegerField(primary_key=True)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name
    
    
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("article_detail", args=[self.id])
    def get_absolute_url(self):
        return reverse("article_detail_slug", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    