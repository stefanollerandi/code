# Generated by Django 4.0.4 on 2022-06-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
