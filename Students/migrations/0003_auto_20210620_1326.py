# Generated by Django 3.1.7 on 2021-06-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_auto_20210620_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topper_list',
            name='stu_rank',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd')], max_length=3),
        ),
        migrations.AlterField(
            model_name='topper_list',
            name='stu_year',
            field=models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Forth Year', 'Forth Year')], max_length=15),
        ),
    ]