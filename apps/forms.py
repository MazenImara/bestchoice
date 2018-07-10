
from django import forms
from .models import Apk



class AppForm(forms.ModelForm):
    class Meta:
        model = Apk
        fields = ['file', 'name', 'os', 'domain', 'port', 'type', 'description']
 

    def __init__(self, *args,**kwargs):
        super(AppForm, self).__init__(*args, **kwargs)