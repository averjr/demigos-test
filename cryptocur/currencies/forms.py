from django import forms
from .models import Currency
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class NewPairForm(forms.Form):
    one = forms.ModelChoiceField(queryset=Currency.objects.all())
    two = forms.ModelChoiceField(queryset=Currency.objects.all())

    def clean_one(self):
        data = self.cleaned_data['one']

        return data

    def clean_two(self):
        data = self.cleaned_data['two']

        if self.cleaned_data['one'] == data:
            raise ValidationError(
                _('Fields values should be different'),
                code='42'
            )
        return data
