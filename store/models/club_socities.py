from django.db import models
from .categories import Category


class ClubSociety(models.Model):
    name=models.CharField(max_length=50)
    slogan=models.CharField(max_length=150)
    description=models.CharField(max_length=600)
    categoryId=models.ForeignKey('Category',on_delete=models.CASCADE,default=1)
    logo=models.ImageField(upload_to='Uploads/Logos')
    price=models.IntegerField(default=0)
    President=models.CharField(max_length=50,null=True,blank=True)

    @staticmethod
    def get_all_ClubSociety():
        return ClubSociety.objects.all()
    
    def get_all_clubsociety_by_id(categoryId):
        if categoryId:
            return ClubSociety.objects.filter(categoryId_id=categoryId)
        else:
            return ClubSociety.get_all_category()
    def get_by_name(name):
        return ClubSociety.objects.filter(name=name)