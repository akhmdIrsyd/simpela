import django_filters
from .models import lahan, pupuk, kabupaten
from django_filters import rest_framework as filters


class LahanFilter(django_filters.FilterSet):
    id_kab = filters.NumberFilter(field_name='id_kab', lookup_expr='exact')
    nama_kab = filters.CharFilter(field_name='id_kab__nama_kab', lookup_expr='contains')

    class Meta():
        model = lahan
        fields = ['id_kab', 'nama_kab']


class PupukFilter(django_filters.FilterSet):
    nama_toko = filters.CharFilter(field_name='nama_toko', lookup_expr='contains')

    class Meta():
        model = pupuk
        fields = ['nama_toko']
