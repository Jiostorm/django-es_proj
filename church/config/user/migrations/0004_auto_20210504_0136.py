# Generated by Django 3.1.8 on 2021-05-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210503_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(max_length=50),
        ),
    ]
