# Generated by Django 3.2.6 on 2021-08-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_myaccount_job_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaccount',
            name='industry',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myaccount',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='myaccount',
            name='skills',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]