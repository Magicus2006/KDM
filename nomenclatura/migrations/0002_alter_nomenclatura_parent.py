# Generated by Django 3.2.6 on 2021-09-02 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclatura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomenclatura',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nomenclatura.folder'),
        ),
    ]
