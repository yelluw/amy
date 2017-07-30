from django import forms


class WorkInquiryContactForm(forms.Form):
    """
    Conact form for work inquiries
    """

    CHOICES = (
            ("1", "I'd like to explore working with Yelluw"),
            ("2", "I have a press inquiry for Yelluw"),
            ("3", "I'd like to grow my personal brand"),
            ("4", "I'm a business owner and want help driving growth"),
        )

    ATTRS = {"class": "form-control"}


    inquiry_type = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES)
    name = forms.CharField(widget=forms.TextInput(attrs=ATTRS), max_length=140)
    email = forms.EmailField(widget=forms.EmailInput(attrs=ATTRS))
    company = forms.CharField(widget=forms.TextInput(attrs=ATTRS), max_length=140)
    phone = forms.CharField(widget=forms.TextInput(attrs=ATTRS), max_length=40)
    message = forms.CharField(widget=forms.Textarea(attrs=ATTRS))

