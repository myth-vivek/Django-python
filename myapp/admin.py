from django.contrib import admin

# Register your models here.
from myapp.models import *

admin.site.register(Category)
admin.site.register(Image)
