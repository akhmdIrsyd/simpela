from django import forms
from .models import pupuk, lahan, User, irigasi
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.models import User


class LoginForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password')

class PupukForm(forms.ModelForm):

    class Meta:
        model = pupuk
        fields = [
            'nama_toko',
            'alamat',
            'Latitude',
            'Longitude',
            'no_tlp',
        ]


class LahanForm(forms.ModelForm):

    class Meta:
        model = lahan
        fields = [
            'id_kab',
            'nama_file',
        ]

class IrigasiForm(forms.ModelForm):

    class Meta:
        model = irigasi
        fields = [
            'id_kab',
            'nama_file',
        ]
