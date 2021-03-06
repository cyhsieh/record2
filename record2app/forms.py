from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms import layout, bootstrap
from record2app.models import Bulletin, Record, TobuyItem, Sport

class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ['bulletin_type', 'title', 'description', 'contact_person', 'phone', 'email', 'image']
    def __init__(self, *args, **kwargs):
        super(BulletinForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = "."
        self.helper.form_methon = "POST"

        #delete empty choice for the tpe
        del self.fields['bulletin_type'].choices[0]

        # self.helper.add_input(Submit('submit', 'Submit'))
        # self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-danger',formnovalidate='formnovalidate'))

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Main data"),
                # layout.Field("bulletin_type"),
                bootstrap.InlineRadios("bulletin_type"),
                layout.Field("title", css_class="input-block-level"),
                layout.Field("description", css_class="input-block-level", rows="3"),
            ),
            layout.Fieldset(
                _("Image"),
                layout.Field("image", css_class="input-block-level"),
                layout.HTML(u""" {% load i18n %}
                        <p class='help-block'>{% trans "Available formats are ..." %}</p>
                    """),
                title=_("Image upload"),
                css_id="image_fieldset",
            ),
            layout.Fieldset(
                _('Contact'),
                layout.Field("contact_person", css_cass="input-block-level"),

                layout.Div(
                    bootstrap.PrependedText("phone", """<span class='glyphicon glyphicon-earphone'></span>""",
                            css_class="input-block-level"),
                    bootstrap.PrependedText("email", "@",
                            placeholder="contact@example.com"),
                    css_id="contact_info",
                ),
            ),
            layout.ButtonHolder(
                    layout.Submit('submit', _('Save')),
                    layout.Submit('cancel', _('Cancel'), css_class='btn-warning',formnovalidate='formnovalidate',)
            )
        )
        



class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields = ['flow_type','item', 'amount', 'purch_date']
    # def __init__(self, *args, **kwargs):
    #     super(RecordForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_action = "."
    #     self.helper.form_method = "POST"
    #     self.helper.layout = layout.Layout(
    #         layout.Fieldset(
    #             'input_field',
    #             'function_field',
    #         )            
    #     ),
    #     layout.ButtonHolder(
    #         Submit('submit', '存檔'),
    #         Submit('cancel', '取消', css_class='btn-warning')
    #     ) 


class DateInput(forms.DateInput):
    input_type = 'date'

class RecordForm2(forms.ModelForm):
    class Meta:
        model=Record
        fields = ['flow_type','item', 'amount', 'purch_date']
        widgets = {
                'purch_date': DateInput()
        }

class RecordForm3(forms.ModelForm):
    class Meta:
        model = Record
        exclude = []
    def __init__(self, *args, **kwargs):
        super(RecordForm3, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['purch_date'].widget = DateInput()
        self.helper.layout = layout.Layout(
                bootstrap.InlineRadios('flow_type'),
                layout.Field('item'),
                layout.Field('amount'),
                layout.Field('purch_date'),
                layout.ButtonHolder(
                    Submit('submit', '送出', css_class='button white'),
                    layout.HTML("<a href='{% url 'list_record' %}' class='btn btn-warning'>取消</a>")
                    )
                )


class TobuyItemForm(forms.ModelForm):
    class Meta:
        model = TobuyItem
        fields = ['itemname', 'budget']

class TobuyForm2(forms.ModelForm):
    class Meta:
        model = TobuyItem
        exclude = []

    def __init__(self, *args, **kwargs):
        super(TobuyForm2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['tobuy_date'].widget = DateInput()
        self.helper.layout = layout.Layout(
                _('待買表單'),
                layout.Field('itemname'),
                layout.Field('budget'),
                layout.Field('tobuy_date'),
                bootstrap.InlineRadios('tobuy_type'),
                # layout.Fieldset(
                    # ),
                layout.ButtonHolder(
                    Submit('submit', '送出', css_class='button white')
                    )
                )
        # fields = ['itemname', 'budget', 'tobuy_type']

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        exclude = []
    def __init__(self, *args, **kwargs):
        super(SportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['sport_date'].widget=DateInput()
        self.helper.layout = layout.Layout(
                # _("運動項目"),
                bootstrap.InlineRadios('user'),
                bootstrap.InlineRadios('sport_item'),
                layout.Field('sport_quantity'),
                bootstrap.InlineRadios('sport_unit'),
                layout.Field('sport_date'),
                layout.ButtonHolder(
                    Submit('submit', '送出')
                    )
                )
