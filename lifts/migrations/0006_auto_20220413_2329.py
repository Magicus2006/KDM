# Generated by Django 3.2.6 on 2022-04-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifts', '0005_calculationtableweightfacade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculationtableweightfacade',
            name='weightFacadeFrom',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='calculationtableweightfacade',
            name='weightFacadeTo',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
