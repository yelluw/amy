from django import forms


class ContactForm(forms.Form):
    """
    Contact form for general inquiries

    TODO:
        - See if using # https://github.com/stefanfoulis/django-phonenumber-field
          is a good choice for this instance.

    """
    inquiry_type = forms.ChoiceField()
    name = forms.CharField(widget=forms.TextInput(attrs={'class': ''}), max_length=140)
    email = forms.EmailFiel(widget=forms.EmailInput(attrs={'class': ''}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class': ''}), max_length=140)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': ''}), max_length=40)
    message = forms.CharField(widget=forms.Textarea(attrs={}))

