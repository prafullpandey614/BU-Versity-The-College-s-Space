from distutils.command.upload import upload
from email import message
from django.db import models
from django.core.validators import MinLengthValidator
# from smart_selects.db_fields import ChainedForeignKey
from .utils import NotesPath , ArticlePath
# Create your models here.
class NewsUpdates(models.Model):
    title = models.CharField(max_length=100)
    date_of_post = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True , db_index=True)
    image_name = models.ImageField(upload_to="Posts/")
    content = models.TextField(validators = [MinLengthValidator(10)])
    
class Semester(models.Model):
    name = models.IntegerField()    
    def __str__(self):
        return f"{self.name}"
    
class Branch(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    semester = models.ManyToManyField(Semester)
    def __str__(self):
        return f"{self.name}"
    
class Subjects(models.Model):
    name = models.CharField(max_length=100) 
    semester = models.ForeignKey(Semester,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.name}"
    
class Notes(models.Model):
    branch_name = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    semester = models.ForeignKey(Semester , on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL,null=True)
    pdf_file = models.FileField(upload_to=NotesPath)
    def __str__(self):
        return f"{self.branch_name} Semester {self.semester}"

class Article(models.Model):
    headline = models.CharField(max_length=30)
    dp_image = models.ImageField(upload_to=ArticlePath)
    update_txt = models.TextField()
    
