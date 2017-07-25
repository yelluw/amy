from django import forms


class ContactForm(forms.Form):
    """
    Contact form for general inquiries
    """
    message = forms.CharField(widget=forms.Textarea(attrs={}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': ''}), max_length=140)
    sender = forms.EmailFiel(widget=forms.EmailInput(attrs={'class': ''}))
