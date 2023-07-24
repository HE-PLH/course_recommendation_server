from django.contrib import admin

from .models import Student, Subject, StudentSubject, StudentWeight, SubjectWeight
# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StudentSubject)
admin.site.register(StudentWeight)
admin.site.register(SubjectWeight)
