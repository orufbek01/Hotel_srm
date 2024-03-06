from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
import qrcode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    age = models.IntegerField(verbose_name='Yosh', default=18)
    phone_number = models.CharField(max_length=13,null=True,blank=True, verbose_name='Telefon raqam' ,validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message = 'Invalide phone number',
            code = 'Invalid number'
        )
    ])
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Famale', 'Famale'),
    )
    gender = models.CharField(max_length=55, verbose_name='Jins', choices=GENDER_CHOICES)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name






class Employee(models.Model):
    full_name = models.CharField(max_length=25, verbose_name="Name")
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Telefon raqamingiz noto'g'ri")])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=25, verbose_name="Gender", choices=GENDER_CHOICES)
    specialty = models.CharField(max_length=25, verbose_name="Specialty")
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()

    def __str__(self):
        return self.full_name


class Cashflow(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=255)
    PAYMENT_TYPE = (
        ('Karta', 'Karta'),
        ('Naqd', 'Naqd'),
    )
    payment_type = models.CharField(max_length=55, choices=PAYMENT_TYPE)
    timestamp = models.DateTimeField(auto_now=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    slugify = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name, self.phone_number)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.Cashflow.user}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

    def __str__(self):
        return self.user

class Pricing(models.Model):
    room_type = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    capacity = models.IntegerField(default=1, verbose_name='Odam_sigmi')
    services = models.CharField(max_length=255, verbose_name='Xonani qulayliklari')
    img = models.ImageField(upload_to='pricing_img/')

    def __str__(self):
        return self.room_type





class Room(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='room_images/')
    description = models.TextField()
    capacity = models.IntegerField()
    contact_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Telefon raqamingiz noto'g'ri")])
    contact_email = models.EmailField(validators=[EmailValidator(message="Email manzilingiz noto'g'ri")])

    class Meta:
        verbose_name = 'Xona'
        verbose_name_plural = 'Xonalar'

    def __str__(self):
        return self.name





class Service(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = 'Xizmatlar'

    def __str__(self):
        return self.name


