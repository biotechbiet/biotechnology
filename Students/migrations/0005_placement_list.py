# Generated by Django 3.1.7 on 2021-06-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0004_project_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='placement_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=70)),
                ('company_name', models.CharField(max_length=120)),
                ('session', models.CharField(max_length=9)),
            ],
        ),
    ]