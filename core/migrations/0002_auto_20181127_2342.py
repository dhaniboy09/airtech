# Generated by Django 2.1.3 on 2018-11-27 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, max_length=200, null=True),
        ),
    ]
