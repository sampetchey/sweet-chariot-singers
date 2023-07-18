from django.db import models

# Create your models here.
class NewsPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
