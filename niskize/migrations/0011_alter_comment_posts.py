# Generated by Django 3.2.4 on 2021-06-10 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niskize', '0010_auto_20210610_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='niskize.posts'),
        ),
    ]