# Generated by Django 3.1.5 on 2021-09-06 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='judul',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
