# Generated by Django 3.1.5 on 2021-09-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_profile_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
