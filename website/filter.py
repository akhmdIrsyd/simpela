import django_filters
from .models import lahan, pupuk, kabupaten, irigasi
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

class IrigasiFilter(django_filters.FilterSet):
    id_kab = filters.NumberFilter(field_name='id_kab', lookup_expr='exact')
    nama_kab = filters.CharFilter(field_name='id_kab__nama_kab', lookup_expr='contains')

    class Meta():
        model = irigasi
        fields = ['id_kab', 'nama_kab']


class KabupatenFilter(django_filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
  
        
class Meta():
        model = kabupaten
        fields = ['id']