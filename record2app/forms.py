from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms import layout, bootstrap
from record2app.models import Bulletin, Record

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
        


class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )
    # def __init__(self, *args, **kwargs):
    #     super(ExampleForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'

    #     self.helper.add_input(Submit('submit', 'Submit'))

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                'first arg is the legend of the fieldset',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                'notes'
            ),
            layout.ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
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
    '''
    def __init__(self, *args, **kwargs):
        super(RecordForm2, self).__init__(*args, **kwargs)
        self.fields['purch_date'].widget.attrs.update({'type':'date'})
        '''
    '''
    def __init__(self, *args, **kwargs):
        super(RecordForm2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = "."
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                'input_field',
                'function_field',
            ),
            layout.Fieldset(
                
            ),
            layout.ButtonHolder(
                Submit('submit', '存檔'),
                Submit('cancel', '取消', css_class='btn-warning')
            )
        )'''

