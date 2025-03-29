from django.contrib import admin
from . import models
from .models import WorkType
admin.site.register(WorkType)

@admin.register(models.FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.FeedBack._meta.get_fields()]
    