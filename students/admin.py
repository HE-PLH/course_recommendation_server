from django.contrib import admin

from .models import Student, Subject, StudentSubject, StudentWeight
# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StudentSubject)
admin.site.register(StudentWeight)
