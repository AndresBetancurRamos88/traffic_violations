# Generated by Django 4.1.7 on 2023-03-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
    ]
