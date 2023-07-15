from django.db import models


class Course(models.Model):
    # course
    course_code = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    years = models.CharField(max_length=255, null=False)
    sem_count = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=255, null=False)


    def __str__(self):
        return "{} ({})".format(self.name, self.category)





