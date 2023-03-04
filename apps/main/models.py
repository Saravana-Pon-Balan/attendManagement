from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    register = models.IntegerField()
    roll_no = models.IntegerField()
    age = models.IntegerField()
    dob = models.DateTimeField()
    department = models.CharField(max_length=200)
    year = models.IntegerField()
    phone = models.IntegerField()
    mail = models.CharField(max_length=200)
    aadhaar_no = models.IntegerField()
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    father_phone = models.IntegerField()
    mother_phone = models.IntegerField()
