from django.contrib import admin
from .models.club_socities import ClubSociety
from .models.categories import Category
from .models.members import Members
# Register your models here.
class AdminClubSociety(admin.ModelAdmin):
    list_display=['name','slogan','price','categoryId','description']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(ClubSociety,AdminClubSociety)
admin.site.register(Category,AdminCategory)
admin.site.register(Members)
