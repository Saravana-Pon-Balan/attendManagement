# Generated by Django 4.1.7 on 2023-03-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_timetable_period_1_remove_timetable_period_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='period',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eight', 'Eight')], max_length=100, null=True),
        ),
    ]
