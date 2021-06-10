from django import forms
from datetime import datetime
from app.models import Exames

class ExamesForm(forms.ModelForm):
    class Meta:
        model = Exames
        fields = ['paciente', 'exame', 'data', 'resultado']


class FieldFormat(forms.Form):
    paciente = forms.CharField(
        widget=forms.TextInput(
            attrs={"style": "text-indent: 7px"}
        )
    )
    exame = forms.CharField(
        widget=forms.TextInput(
            attrs={"style": "text-indent: 7px"}
        )
    )
    data = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local",
            "min": datetime.now().strftime('%Y-%m-%dT%H:%M'),
            "style": "text-indent: 3px"
            }
        )
    )
    resultado = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"style": "text-indent: 7px; resize: none", "rows": 5, "cols": 28}
        )
    )