# Generated by Django 4.1 on 2023-04-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_alter_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Door_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
