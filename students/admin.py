from django.contrib import admin

from .models import Student, Subject, StudentSubject
# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StudentSubject)
