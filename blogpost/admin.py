from django.contrib import admin
from .models import SampleModels, BlogModel

# Register your models here.

admin.site.register(SampleModels)
admin.site.register(BlogModel)
