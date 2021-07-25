from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import User, pupuk, lahan, kabupaten, irigasi
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(User)
admin.site.register(pupuk)
admin.site.register(lahan)
admin.site.register(kabupaten)
admin.site.register(irigasi)

