# Generated by Django 3.2.6 on 2021-08-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_myaccount_show_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='myaccount',
            name='profile_completed',
            field=models.BooleanField(default=False),
        ),
    ]
