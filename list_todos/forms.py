from django import forms
from .models import List


class ToDoListForm(forms.ModelForm):
    """docstring for ClassName"""

    class Meta:
        model = List
        fields = ["item", "completed"]
