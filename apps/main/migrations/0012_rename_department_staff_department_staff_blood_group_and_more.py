# Generated by Django 4.1.7 on 2023-03-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_employee_name_staff_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='department',
            new_name='Department',
        ),
        migrations.AddField(
            model_name='staff',
            name='Blood_group',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Community',
            field=models.CharField(choices=[('OC', 'OC'), ('BC', 'BC'), ('MBC', 'MBC'), ('SC\\ST', 'SC\\ST'), ('Other', 'Other')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='District',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Door_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Experience',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Father_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Marital_Status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Mode_of_Transpotation',
            field=models.CharField(choices=[('College bus', 'College bus'), ('Own vehicle', 'Own vehicle'), ('By walk', 'By walk')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Mother_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Qualification',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Religion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Spouse_Name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='State',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='Street_and_Village',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='aadhaar_no',
            field=models.IntegerField(null=True),
        ),
    ]
