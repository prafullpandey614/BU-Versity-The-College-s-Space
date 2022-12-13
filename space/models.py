from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Semester(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    sem=models.CharField(max_length=1,null=True)
    def __str__ (self):
        return self.sem

class Branch(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    branch=models.CharField(max_length=15,null=True)
    def __str__ (self):
        return self.branch
class Year(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    year=models.CharField(max_length=15,null=True)
    def __str__ (self):
        return self.year

class Paper(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    year=models.ForeignKey(Year,on_delete=models.CASCADE,null=True)
    paper_name=models.CharField(max_length=20,null=True)
    paper_pdf=models.FileField(upload_to="paper/",null=True,default=None)
 
class Syllabus(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    syllabus_pdf=models.FileField(upload_to="syllabus/",null=True,default=None)