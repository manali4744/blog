# Generated by Django 3.2.18 on 2023-04-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeblog', '0003_remove_blogwrite_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogwrite',
            name='like',
            field=models.ManyToManyField(to='writeblog.Like'),
        ),
    ]