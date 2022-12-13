from django.contrib import admin
from .models import NewsUpdates ,Article , Semester ,Subjects,Branch,Notes
# Register your models here.
admin.site.register(NewsUpdates)
admin.site.register(Semester)
admin.site.register(Branch)
admin.site.register(Notes)
admin.site.register(Subjects)
admin.site.register(Article)
