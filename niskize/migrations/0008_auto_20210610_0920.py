# Generated by Django 3.2.4 on 2021-06-10 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('niskize', '0007_alter_posts_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='comment',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='niskize.posts')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
