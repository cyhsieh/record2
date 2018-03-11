from django.shortcuts import render, redirect
from record2app import forms
from record2app.models import Bulletin, Record

# Create your views here.
def new_bulletin(request):
    if request.method == "POST":
        form = forms.BulletinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list_bulletin')
        else:
            message = "驗證錯誤"
    else:
        form = forms.BulletinForm()
        title = "This is record2 hello"
        return render(request, "hello.html", locals())


def list_bulletin(request):
    posts = Bulletin.objects.all().order_by('-id')
    return render(request, "list_bulletin.html", locals())

def edit_bulletin(request,id=None):
    if request.method=="POST":
        #from edit form to save
        if 'cancel' in request.POST:
            return redirect('/list_bulletin')
        else:
            edit_post = Bulletin.objects.get(id=id)
            form = forms.BulletinForm(request.POST, instance=edit_post)
            if form.is_valid():
                form.save()
                return redirect('/list_bulletin')
            else:
                message = "驗證錯誤"
    else:
        #from url to edit form
        title = "edit_bulletin page"
        edit_post = Bulletin.objects.get(id=id)
        edit_form = forms.BulletinForm(instance=edit_post)
        return render(request, "edit_bulletin.html", locals())





def list_record(request):
    title = "List record Page"
    records = Record.objects.all().order_by('-id')
    return render(request, "list_record.html", locals()) 

def new_record(request):
    title = "new record page"
    record_form= forms.RecordForm()
    return render(request, "new_record.html", locals())

