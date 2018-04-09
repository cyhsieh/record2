from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
from testapp.models import testmodel
from datetime import datetime, date

class testform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(testform, self).__init__(*args, **kwargs)
        self.fields['testdate'].initial = date.today()
    class Meta:
        model = testmodel
        fields = ['testdate', 'testmail', 'testtext']
