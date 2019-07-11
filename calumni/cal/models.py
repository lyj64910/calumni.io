from django.db import models

# Create your models here.
class Cal(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("data published")
    image = models.ImageField(upload_to='images/', blank=True)