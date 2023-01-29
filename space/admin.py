from django.contrib import admin
<<<<<<< HEAD
from .models import NewsUpdates  , Semester ,Subjects,Branch,Notes,ContactMessage ,PreviousYearQuestions
=======
from .models import NewsUpdates ,Article , Semester ,Subjects,Branch,Notes
>>>>>>> a05e8fef204af0f4a54ef349eaaf41719d2c3fc5
# Register your models here.
admin.site.register(NewsUpdates)
admin.site.register(Semester)
admin.site.register(Branch)
admin.site.register(Notes)
admin.site.register(Subjects)
<<<<<<< HEAD
admin.site.register(PreviousYearQuestions)
admin.site.register(ContactMessage)
=======
admin.site.register(Article)
>>>>>>> a05e8fef204af0f4a54ef349eaaf41719d2c3fc5
