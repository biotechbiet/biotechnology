# Generated by Django 3.1.7 on 2021-06-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0003_auto_20210620_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=9)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
