# Generated by Django 3.1.3 on 2020-11-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='IC_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='family_dependent',
        ),
        migrations.RemoveField(
            model_name='student',
            name='family_income',
        ),
        migrations.RemoveField(
            model_name='student',
            name='matric_no',
        ),
        migrations.AlterField(
            model_name='student',
            name='registration_number',
            field=models.IntegerField(unique=True),
        ),
    ]
