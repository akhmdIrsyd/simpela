from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('lahan', views.lahanViewSet, basename='api_lahan')
router.register('pupuk', views.pupukViewSet, basename='api_pupuk')
router.register('irigasi', views.IrigasiViewSet, basename='api_irigasi')
router.register('kabupaten', views.KabupatenViewSet, basename='api_kabupaten')



urlpatterns = [
    #user
    path('', views.index_user, name='home'),
    path('user_lahan', views.user_lahan, name='user_lahan'),
    path('user_pupuk', views.user_pupuk, name='user_pupuk'),
    path('user_irigasi', views.user_irigasi, name='user_irigasi'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),

    #dashboard
    path('dashboard', views.index, name='dashboard'),
    path('show_lahan', views.show_lahan, name='show_lahan'),
    path('lahan_view', views.lahan_view, name='lahan_view'),
    path('add_lahan', views.add_lahan, name='add_lahan'),
    path('update_lahan/<int:pk>/', views.update_lahan, name='update_lahan'),
    path('Delete_lahan/<int:pk>/', views.Delete_lahan, name='Delete_lahan'),
    path('pupuk_view', views.pupuk_view, name='pupuk_view'),
    path('add_pupuk', views.add_pupuk, name='add_pupuk'),
    path('update_pupuk/<int:pk>/', views.update_pupuk, name='update_pupuk'),
    path('show_pupuk', views.show_pupuk, name='show_pupuk'),
    path('Delete_pupuk/<int:pk>/', views.Delete_pupuk, name='Delete_pupuk'),
    path('show_irigasi', views.show_irigasi, name='show_irigasi'),
    path('irigasi_view', views.irigasi_view, name='irigasi_view'),
    path('add_irigasi', views.add_irigasi, name='add_irigasi'),
    path('update_irigasi/<int:pk>/', views.update_irigasi, name='update_irigasi'),
    path('Delete_irigasi/<int:pk>/', views.Delete_irigasi, name='Delete_irigasi'),

    path('api/', include(router.urls))
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
