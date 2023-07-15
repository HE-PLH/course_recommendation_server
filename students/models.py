from django.db import models

import sys
sys.path.append("..")

from chatbot.models import Responses

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

    subject = models.CharField(max_length=255, null=False)
    grade = models.CharField(max_length=255, null=False)


    def __str__(self):
        return "{} - {} - {}".format(self.subject, self.grade, self.user)

class StudentWeights(models.Model):
    # subject
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    response = models.ForeignKey(Responses, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user, self.response)





