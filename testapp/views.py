from django.shortcuts import render
from testapp import forms
from testapp.models import testmodel

# Create your views here.

def testindex(request):
    form = forms.testform()
    return render(request,"test/test.html", locals())
