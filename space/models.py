from re import L
from turtle import position
from django.db import models
from django.core.validators import MinLengthValidator

from .utils import NotesPath , ArticlePath ,PyqPath


class JobsModel(models.Model):
    titles = models.CharField(max_length=30)
    position = models.CharField(max_length=30,blank=True)
    date = models.DateField(auto_now_add=True)
    link = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name}  {self.date}"

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
    
class PreviousYearQuestions(models.Model):
    year = models.IntegerField(default=2020)
    branch_name = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester,on_delete=models.SET_NULL,null=True)
    pdf_file = models.FileField(upload_to=PyqPath ,null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.year}:{self.branch_name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"{self.name}  {self.email}"

class ClubMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    registration_id = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    level_of_interest = models.CharField(max_length=255)
    reason_to_select = models.CharField(max_length=255)