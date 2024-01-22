# Generated by Django 4.2.6 on 2024-01-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
    ]