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
    title = "記帳紀錄"
    records = Record.objects.all().order_by('-purch_date', '-create_date')
    return render(request, "list_record.html", locals()) 


'''
def new_record(request):
    title = "新增紀錄"
    record_form= forms.RecordForm()
    return render(request, "new_record.html", locals())
    '''

def new_record2(request):
    title = "新增紀錄"
    if request.method == "POST":
        form = forms.RecordForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list_record')
        else:
            message = "驗證錯誤！"
    else:
        record_form = forms.RecordForm2()
        return render(request, "new_record2.html", locals())

def edit_record(request, id=None):
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect('/list_record')
        # receive edit form
        else:
            edit_rec = Record.objects.get(id=id)
            form = forms.RecordForm2(request.POST, instance=edit_rec)
            if form.is_valid():
                form.save()
                return redirect('/list_record')
    # from url
    else:
        title = "編輯紀錄"
        edit_rec = Record.objects.get(id=id)
        edit_form = forms.RecordForm2(instance=edit_rec)
        return render(request, "edit_record.html", locals())





