# Generated by Django 2.1.3 on 2018-12-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20181201_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='gate',
            field=models.CharField(default='TBD', max_length=50),
        ),
    ]