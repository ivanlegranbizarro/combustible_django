from django import forms
from .models import Mark


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ["description"]

    def __init__(self, *args, **kwargs):
        super(MarkForm, self).__init__(*args, **kwargs)
        self.fields["description"].widget.attrs.update({"class": "form-control"})
