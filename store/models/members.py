from django.db import models
from django.db.models.base import Model

class Members(models.Model):
    firstname=models.CharField(max_length=15,null=True, blank=True)
    lastname=models.CharField(max_length=10,null=True, blank=True)
    mobile=models.CharField(max_length=10,null=True, blank=True)
    email=models.EmailField()
    password=models.CharField(max_length=500,null=True, blank=True)

    def register(self):
        self.save()

    def isExist(self):
        if Members.objects.filter(email=self.email):
            return True
        else:
            return False