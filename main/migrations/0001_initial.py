# Generated by Django 4.1.13 on 2024-03-06 14:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.IntegerField(default=18, verbose_name='Yosh')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Invalide phone number', regex='^[\\+]9{2}8{1}[0-9]{9}$')], verbose_name='Telefon raqam')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Famale', 'Famale')], max_length=55, verbose_name='Jins')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', message="Telefon raqamingiz noto'g'ri")])),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=25, verbose_name='Gender')),
                ('specialty', models.CharField(max_length=25, verbose_name='Specialty')),
                ('start_work_time', models.TimeField()),
                ('end_work_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('capacity', models.IntegerField(default=1, verbose_name='Odam_sigmi')),
                ('services', models.CharField(max_length=255, verbose_name='Xonani qulayliklari')),
                ('img', models.ImageField(upload_to='pricing_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='room_images/')),
                ('description', models.TextField()),
                ('capacity', models.IntegerField()),
                ('contact_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', message="Telefon raqamingiz noto'g'ri")])),
                ('contact_email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message="Email manzilingiz noto'g'ri")])),
            ],
            options={
                'verbose_name': 'Xona',
                'verbose_name_plural': 'Xonalar',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Xizmat',
                'verbose_name_plural': 'Xizmatlar',
            },
        ),
        migrations.CreateModel(
            name='Cashflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.CharField(max_length=255)),
                ('payment_type', models.CharField(choices=[('Karta', 'Karta'), ('Naqd', 'Naqd')], max_length=55)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('slugify', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
