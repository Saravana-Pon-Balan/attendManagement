from django.db import models

dept_choices = [
    ('Computer Science and Engineering','CSE'),
    ('Electronics and Communication Engineering','ECE'),
    ('Electrical and Electronic Engineering','EEE'),
    ('Mechanical Engineering','Mech'),
    ('Civil Engineering','Civil')
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

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    DOB = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    department = models.CharField(max_length=200, choices=dept_choices)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TimeTable(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    day = models.CharField(max_length=50)
    period_1 = models.CharField(max_length=50)
    period_2 = models.CharField(max_length=50)
    period_3 = models.CharField(max_length=50)
    period_4 = models.CharField(max_length=50)
    period_5 = models.CharField(max_length=50)
    period_6 = models.CharField(max_length=50)
    period_7 = models.CharField(max_length=50)
    period_8 = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.department} - {self.year} - {self.day}'

