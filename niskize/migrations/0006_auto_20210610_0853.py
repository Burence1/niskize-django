# Generated by Django 3.2.4 on 2021-06-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niskize', '0005_auto_20210609_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=120, null=True),
        ),
    ]