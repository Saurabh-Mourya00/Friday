from django.contrib import admin

# Register your models here.
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile,ProfileAdmin)