from django.shortcuts import render, redirect, get_object_or_404
from django import forms as djforms
from record2app import forms
from record2app.models import Bulletin, Record, TobuyItem
from django.views.generic import ListView, DetailView
from record2app.recParser import Rec_parser

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

def recordform(request, pk=None, template_name="record2app/recordform.html"):
    record = Record()
    try:
        record = Record.objects.get(id=pk)
        title = "修改紀錄"
    except:
        title = "新增紀錄"
    form = forms.RecordForm3(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('list_record')
    return render(request, template_name, locals())


def new_record_cli(request):
    title = "文字新增記帳"
    if request.method=="POST":
        # received date => transfer rec
        enter_text = request.POST['enter_area']
        result_text = "you entered is:\n"+enter_text
        result_text = rec_parse(enter_text)
        return render(request, "new_record_cli.html", locals())
    else:
        #blank cli page
        return render(request, "new_record_cli.html", locals())

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

def delete_record(request, id=None):
    del_rec = Record.objects.get(id=id)
    del_rec.delete()
    return redirect('/list_record')

class RecordListView(ListView):
    model = Record

class RecordDetailView(DetailView):
    # context_object_name = 'record'
    # queryset = Record.objects.all()
    model = Record

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record_list'] = Record.objects.all()
        return context

def rec_parse(rec_lines):
    result = ""
    Parser = Rec_parser()
    for line in rec_lines.splitlines():
        # result = result + Rec_parser.rec_match(line) + "\n"
        parsed_rec = Parser.rec_match(line)
        # fulldate = 
        if parsed_rec['pat_name'] == 'payrec':
            pass
            # result = result + "%s"
        
        for key in parsed_rec:
            result = result + key + ":" + parsed_rec[key] + "\n"
        result=result+"---------\n"
    return result

class TobuyItemView(ListView):
    model = TobuyItem
    context_object_name = 'tobuyitems'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "待買項目"
        return context
# class TobuyForm(forms.

def TobuyForm(request,pk=None, template_name="record2app/tobuyform.html"):
    # tobuyitem = get_object_or_404(TobuyItem, id=pk)
    # tobuyitem = TobuyItem.objects.get(id=pk)
    tobuyitem = TobuyItem()
    try:
        tobuyitem = TobuyItem.objects.get(id=pk)
        title = "修改待買項目"
    except:
        title = "新增待買項目"
    # form = forms.TobuyItemForm(request.POST or None, instance=tobuyitem)
    form = forms.TobuyForm2(request.POST or None, instance=tobuyitem)
    if form.is_valid():
        form.save()
        return redirect("list_tobuy")
    return render(request, template_name, locals())

