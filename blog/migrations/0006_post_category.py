# Generated by Django 4.2.6 on 2023-11-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]
