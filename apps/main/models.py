from django.db import models

dept_choices = [
    ('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('Mech','Mech'),('Civil','Civil')
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


class Subject(models.Model):
    year_choices = [(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year')]
    sem_choices = [('odd', 'Odd'), ('even', 'Even')]
    department = models.CharField(choices=dept_choices,max_length=100,null=True,default='CSE')
    year = models.IntegerField(choices=year_choices)
    sem  = models.CharField(max_length=20,choices=sem_choices)
    name = models.CharField(max_length=50,null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.name


class TimeTable(models.Model):
    day = models.CharField(max_length=50)
    period_1 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='period_1', null=True)
    period_2 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='period_2', null=True)
    period_3 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='period_3', null=True)
    period_4 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='period_4', null=True)
    period_5 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='period_5', null=True)
    period_6 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='period_6', null=True)
    period_7 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='period_7', null=True)
    period_8 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='period_8', null=True)

    def __str__(self):
        return f'{self.period_1.year} {self.period_1.department} {self.day}'

