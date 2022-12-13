from django.contrib import admin
from .models import Branch,Paper,Semester,Year,Syllabus
# Register your models here.
@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display= ['user', 'sem']

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display= ['user', 'branch']

@admin.register(Year)
class BranchAdmin(admin.ModelAdmin):
    list_display= ['user', 'year']

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display= ['branch', 'sem', 'year', 'paper_name', 'paper_pdf']

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display= ['branch', 'sem', 'syllabus_pdf']
