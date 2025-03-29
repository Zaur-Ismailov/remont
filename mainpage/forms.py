from django import forms
from . import models
from .models import SelectedWork, WorkType

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = models.FeedBack
        fields = [field.name for field in models.FeedBack._meta.get_fields()]

class WorkSelectionForm(forms.Form):
    work_type = forms.ModelChoiceField(queryset=WorkType.objects.all())
    area = forms.DecimalField(min_value=0.1, max_digits=10, decimal_places=2)

class SelectedWorkForm(forms.ModelForm):
    class Meta:
        model = SelectedWork
        fields = ['work_type', 'area']