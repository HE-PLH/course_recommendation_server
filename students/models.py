from django.db import models


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





