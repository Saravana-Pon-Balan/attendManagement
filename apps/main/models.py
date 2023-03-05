from django.db import models

dept_choices = [
    ('CSE', 'Computer Science and Engineering'),
    ('ECE', 'Electronics and Communication Engineering'),
    ('EEE', 'Electrical and Electronic Engineering'),
    ('Mech', 'Mechanical Engineering'),
    ('Civil', 'Civil Engineering')
]


class Student(models.Model):
    name = models.CharField(max_length=200)
    register = models.IntegerField()
    roll_no = models.IntegerField()
    age = models.IntegerField()
    DOB = models.DateField(null=True)
    department = models.CharField(max_length=200, choices=dept_choices)
    year = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    aadhaar_no = models.IntegerField()
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    father_phone = models.IntegerField()
    mother_phone = models.IntegerField()


class Staff(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    DOB = models.DateField(null=True)
    phone = models.IntegerField()
    department = models.CharField(max_length=200, choices=dept_choices)
