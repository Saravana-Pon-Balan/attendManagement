# Generated by Django 4.1 on 2023-03-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_department_year_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL')], max_length=50),
        ),
    ]