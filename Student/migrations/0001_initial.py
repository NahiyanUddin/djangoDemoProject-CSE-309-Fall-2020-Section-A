# Generated by Django 3.1.6 on 2021-03-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(db_column='Student ID', max_length=8)),
                ('student_name', models.CharField(db_column='Student Name', max_length=25)),
                ('email', models.EmailField(db_column='Email', max_length=19)),
                ('section', models.CharField(db_column='Section', max_length=2)),
            ],
            options={
                'db_table': 'Student-info',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(db_column='Student ID', max_length=8)),
                ('student_name', models.CharField(db_column='Student Name', max_length=25)),
                ('email', models.EmailField(db_column='Email', max_length=19)),
                ('section', models.CharField(db_column='Section', max_length=2)),
            ],
        ),
    ]
