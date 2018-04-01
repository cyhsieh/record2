from django import forms
from django.utils.translation import ugettext_lazy as _

from movies.models import Genre
from movies.models import Director
from movies.models import Actor
from movies.models import RATING_CHOICES

class MovieFilterForm(forms.Form):
    genre = forms.ModelChoiceField(
            label=_("Genre"),
            required=False,
            queryset=Genre.objects.all(),
    )
    director = forms.ModelChoiceField(
            label=_("Director"),
            required=False,
            queryset=Director.objects.all(),
     )
    actor = forms.ModelChoiceField(
            label=_("Actor"),
            required=False,
            queryset=Actor.objects.all(),
    )
    rating = forms.ChoiceField(
            label=_("Rating"),
            required=False,
            choices=RATING_CHOICES,
    )
