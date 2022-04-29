# Generated by Django 3.2.5 on 2021-08-07 18:02

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MyAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('stripe_customer_id', models.CharField(
                    blank=True, max_length=150, null=True, unique=True)),
                ('stripe_subscription_id', models.CharField(
                    blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('package_tier', models.IntegerField(default=1)),
                ('package_name', models.CharField(
                    default='Free Account', max_length=50)),
                ('date_joined', models.DateTimeField(
                    auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(
                    auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True,
                    default=users.models.get_default_profile_image,
                 null=True, upload_to=users.models.get_profile_image_filepath)),
                ('job_role', models.CharField(blank=True,
                 default='', max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('skills', models.CharField(blank=True,
                 default='', max_length=1000, null=True)),
                ('hide_email', models.BooleanField(default=True)),
                ('location', models.CharField(blank=True,
                 default='', max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True,
                 help_text=f'The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user',
                 to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
