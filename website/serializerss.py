# serializers
from rest_framework import serializers
from .models import pupuk,lahan,kabupaten,irigasi

class KabSerializer(serializers.ModelSerializer):
    class Meta:
        model = kabupaten
        fields = '__all__'

class PupukSerializer(serializers.ModelSerializer):
    class Meta:
        model = pupuk
        fields = '__all__'


class LahanSerializer(serializers.ModelSerializer):
    #id_kabupaten = KabSerializer(source='id_kab', read_only=True)
    nama_kab = serializers.CharField(source='id_kab.nama_kab', read_only=True)
    class Meta:
        model = lahan
        fields = '__all__'


class IrigasiSerializer(serializers.ModelSerializer):
    #id_kabupaten = KabSerializer(source='id_kab', read_only=True)
    nama_kab = serializers.CharField(source='id_kab.nama_kab', read_only=True)
    class Meta:
        model = irigasi
        fields = '__all__'


