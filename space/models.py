from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class NewsUpdates(models.Model):
    title = models.CharField(max_length=100)
    date_of_post = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True , db_index=True)
    image_name = models.ImageField(upload_to="Posts/")
    content = models.TextField(validators = [MinLengthValidator(10)])
    