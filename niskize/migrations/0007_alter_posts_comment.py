# Generated by Django 3.2.4 on 2021-06-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niskize', '0006_auto_20210610_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='comment',
            field=models.TextField(default='', null=True),
        ),
    ]