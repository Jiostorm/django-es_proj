# Generated by Django 3.1.8 on 2021-05-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210503_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('M', 'Man'), ('F', 'Woman')], max_length=1, null=True),
        ),
    ]
