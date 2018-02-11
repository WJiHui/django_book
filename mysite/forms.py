# encoding:utf-8
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='主题 ')
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            # this error will join in form.errors
            raise forms.ValidationError("Not enough words!")
        return message
