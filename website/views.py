from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, HttpResponse

from .forms import PupukForm, LahanForm, IrigasiForm
from .models import pupuk,User,lahan,kabupaten, irigasi

from django.core import serializers
# Create your views here.


from django.views import generic


from django.contrib.auth.hashers import make_password
from django.contrib import messages

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required

from .serializerss import LahanSerializer,PupukSerializer,IrigasiSerializer,KabSerializer
from rest_framework import routers, serializers, viewsets
from .filter import LahanFilter, PupukFilter, IrigasiFilter,KabupatenFilter
from django_filters import rest_framework as filters


@csrf_protect
def Login(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')  # Get email value from form
        password = request.POST.get('password')  # Get password value from form
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_authenticated:
                return redirect('dashboard')  
        else:
            # Invalid email or password. Handle as you wish
            return redirect('login')

    return render(request, 'user/login.html')

def Logout(request):
    logout(request)
    return redirect('home')
# Create your views here.
#user


class lahanViewSet(viewsets.ModelViewSet):
    queryset = lahan.objects.all()
    serializer_class = LahanSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = LahanFilter


class pupukViewSet(viewsets.ModelViewSet):
    queryset = pupuk.objects.all()
    serializer_class = PupukSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PupukFilter

class IrigasiViewSet(viewsets.ModelViewSet):
    queryset = irigasi.objects.all()
    serializer_class = IrigasiSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = IrigasiFilter

class KabupatenViewSet(viewsets.ModelViewSet):
    queryset = kabupaten.objects.all()
    serializer_class = KabSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = KabupatenFilter


def index_user(request):
    #Data_siswa = data_siswa.objects.all()
    context = {
    }
    return render(request, 'user/home.html', context)

def user_lahan(request):
    Data_kab = kabupaten.objects.values()
    Data_lahan = lahan.objects.values()
    Data_lahan = list(Data_lahan)
    context = {
        'data': Data_lahan,
        'rows': Data_kab,
    }
    return render(request, 'user/lahan.html', context)


def user_pupuk(request):
    Data_pupuk = pupuk.objects.values()
    Data_pupuk = list(Data_pupuk)
    context = {
        'data': Data_pupuk,
    }
    return render(request, 'user/pupuk.html', context)

def user_irigasi(request):
    Data_kab = kabupaten.objects.values()
    Data_irigasi = irigasi.objects.values()
    Data_irigasi = list(Data_irigasi)
    context = {
        'data': Data_irigasi,
        'rows': Data_kab,
    }
    return render(request, 'user/irigasi.html', context)



#dashboard
@login_required(login_url='/')
def index(request):
    #Data_siswa = data_siswa.objects.all()
    context = {
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='/')
def show_lahan(request):
    Data_kab = kabupaten.objects.values()
    Data_lahan = lahan.objects.values()
    Data_lahan = list(Data_lahan)
    context = {
        'data': Data_lahan,
        'rows': Data_kab,
    }
    return render(request, 'dashboard/show_lahan.html', context)


@login_required(login_url='/')
def lahan_view(request):
    Data_lahan = lahan.objects.all()
    context = {
        'rows': Data_lahan,
    }
    return render(request, 'dashboard/lahan.html', context)


@login_required(login_url='/')
def add_lahan(request):
    if request.method == 'POST':
        form = LahanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lahan_view')
    else:
        form = LahanForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/forms.html', context)


@login_required(login_url='/')
def update_lahan(request, pk):

    Data_lahan = lahan.objects.get(id=pk)
    if request.method == 'POST':
        form = LahanForm(
            request.POST, request.FILES, instance=Data_lahan)
        if form.is_valid():
            form.save()
            return redirect('lahan_view')
    else:
        form = LahanForm(instance=Data_lahan)
    context = {
        'form': form,
        'rows': Data_lahan
    }
    return render(request, 'dashboard/forms.html', context)


@login_required(login_url='/')
def Delete_lahan(request, pk):
    Data_lahan = lahan.objects.get(id=pk)
    Data_lahan.delete()
    return redirect('lahan_view')

# Perkontolan

@login_required(login_url='/')
def show_irigasi(request):
    Data_kab = kabupaten.objects.values()
    Data_irigasi = irigasi.objects.values()
    Data_irigasi = list(Data_irigasi)
    context = {
        'data': Data_irigasi,
        'rows': Data_kab,
    }
    return render(request, 'dashboard/show_irigasi.html', context)


@login_required(login_url='/')
def irigasi_view(request):
    Data_irigasi = irigasi.objects.all()
    context = {
        'rows': Data_irigasi,
    }
    return render(request, 'dashboard/irigasi.html', context)


@login_required(login_url='/')
def add_irigasi(request):
    if request.method == 'POST':
        form = IrigasiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('irigasi_view')
    else:
        form = IrigasiForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/forms.html', context)


@login_required(login_url='/')
def update_irigasi(request, pk):

    Data_irigasi = irigasi.objects.get(id=pk)
    if request.method == 'POST':
        form = IrigasiForm(
            request.POST, request.FILES, instance=Data_irigasi)
        if form.is_valid():
            form.save()
            return redirect('irigasi_view')
    else:
        form = IrigasiForm(instance=Data_irigasi)
    context = {
        'form': form,
        'rows': Data_irigasi
    }
    return render(request, 'dashboard/forms.html', context)


@login_required(login_url='/')
def Delete_irigasi(request, pk):
    Data_irigasi = irigasi.objects.get(id=pk)
    Data_irigasi.delete()
    return redirect('irigasi_view')

# perkontolan end
@login_required(login_url='/')
def show_pupuk(request):
    Data_pupuk = pupuk.objects.values()
    Data_pupuk = list(Data_pupuk)
    context = {
        'data': Data_pupuk,
    }
    return render(request, 'dashboard/show_pupuk.html', context)


@login_required(login_url='/')
def pupuk_view(request):
    Data_pupuk = pupuk.objects.all()
    context = {
        'rows': Data_pupuk,
    }
    return render(request, 'dashboard/pupuk.html', context)


@login_required(login_url='/')
def add_pupuk(request):
    if request.method == 'POST':
        form = PupukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pupuk_view')
    else:
        form = PupukForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/forms.html', context)


@login_required(login_url='/')
def update_pupuk(request, pk):
    
    Data_pupuk = pupuk.objects.get(id=pk)
    if request.method == 'POST':
        form = PupukForm(
            request.POST, instance=Data_pupuk)
        if form.is_valid():
            form.save()
            return redirect('pupuk_view')
    else:
        form = PupukForm(instance=Data_pupuk)
    context = {
        'form': form,
        'rows': Data_pupuk
    }
    return render(request, 'dashboard/forms.html', context)


@login_required(login_url='/')
def Delete_pupuk(request, pk):
    Data_pupuk = pupuk.objects.get(id=pk)
    Data_pupuk.delete()
    return redirect('pupuk_view')

