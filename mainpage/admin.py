from django.contrib import admin
from . import models

@admin.register(models.FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.FeedBack._meta.get_fields()]
    