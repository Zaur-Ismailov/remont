from django import forms
from . import models

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = models.FeedBack
        fields = [field.name for field in models.FeedBack._meta.get_fields()]

