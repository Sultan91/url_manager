from django import forms
from .models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = [
            'text'
        ]

    def clean(self):
        super(UrlForm, self).clean()
        # extracting fields
        text = self.cleaned_data.get('text')
        # check if it is an url
        if 'http' not in text:
            self.errors['text'] = self.error_class([
                'Please include valid URL '
            ])
        return self.cleaned_data