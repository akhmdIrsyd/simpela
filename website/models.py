
# Create your models here.
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver

from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'user'),
        (2, 'admin'),
    )
    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=1)
    username = None
    email = models.EmailField(_('email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    
def _upload_path(instance, filename):
    return instance.get_upload_path(filename)

def file_size(value):  # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')


class pupuk(models.Model):
    nama_toko = models.CharField(max_length=50, verbose_name='Nama Toko')
    alamat = models.TextField(blank=True, null=True)
    Latitude = models.FloatField(max_length=50, verbose_name='Latitude')
    Longitude = models.FloatField(max_length=50, verbose_name='Longitude')
    no_tlp = models.CharField(max_length=50,  verbose_name='Nomor Telpon')

    def __str__(self):
        return str(self.id)


class kabupaten(models.Model):

    nama_kab = models.CharField(max_length=50, verbose_name='Nama kabupaten')
    Latitude = models.FloatField(max_length=50, verbose_name='Latitude')
    Longitude = models.FloatField(max_length=50, verbose_name='Longitude')

    def __str__(self):
        return str(self.nama_kab)

class lahan(models.Model):

    id_kab = models.ForeignKey(kabupaten, on_delete=models.CASCADE, verbose_name='Nama kabupaten')
    nama_file = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['kmz']), file_size])

    def get_upload_path(self, filename):
        return str("lahan/"+self.id_kab.nama_kab)+"/"+filename
    def __str__(self):
        return str(self.id_kab)

class irigasi(models.Model):

    id_kab = models.ForeignKey(kabupaten, on_delete=models.CASCADE, verbose_name='Nama kabupaten')
    nama_file = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['kmz']), file_size])

    def get_upload_path(self, filename):
        return str("irigasi/"+self.id_kab.nama_kab)+"/"+filename
    def __str__(self):
        return str(self.id_kab)