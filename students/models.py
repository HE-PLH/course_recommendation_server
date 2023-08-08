from django.db import models

import sys
sys.path.append("..")

from chatbot.models import Responses
from courses.models import Course

class Student(models.Model):
    # student
    index = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    firstname = models.CharField(max_length=255, null=False)
    middlename = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    school = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)


    def __str__(self):
        return "{} - {}".format(self.firstname, self.middlename)


class Subject(models.Model):
    # subject
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}".format(self.name)

class StudentSubject(models.Model):
    # subject
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=255, null=False)


    def __str__(self):
        return "{} - {} - {}".format(self.subject, self.grade, self.user)

class StudentWeight(models.Model):
    # subject
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    response = models.ForeignKey(Responses, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user, self.response)

class SubjectWeight(models.Model):
    # s_weight
    grade = models.CharField(max_length=255, null=False)
    value = models.FloatField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "{} . {} . {} . {}".format(self.subject, self.grade, self.value, self.course)



class StudentResponses(models.Model):
    # s_response
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    response = models.ForeignKey(Responses, on_delete=models.CASCADE)


    def __str__(self):
        return "{} . {}".format(self.response, self.user)


