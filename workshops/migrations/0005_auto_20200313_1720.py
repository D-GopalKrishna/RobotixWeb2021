# Generated by Django 2.1.7 on 2020-03-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0004_auto_20200312_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='semester',
            field=models.CharField(max_length=20),
        ),
    ]