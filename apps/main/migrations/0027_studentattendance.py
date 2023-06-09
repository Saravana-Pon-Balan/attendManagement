# Generated by Django 4.1.7 on 2023-03-22 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_staff_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('mark_attendance', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('On Duty', 'On Duty')], max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.timetable')),
            ],
        ),
    ]
