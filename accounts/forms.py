from django import forms
from .models import TribalYouth

class AddCaptionForm(forms.ModelForm):
    class Meta:
        model = TribalYouth
        fields = ['caption']