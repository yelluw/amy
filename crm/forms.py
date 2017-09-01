from django import forms


class WorkInquiryContactForm(forms.Form):
    """
    Contact form for work inquiries
    """

    CHOICES = (
            ("general", "I'd like to explore working with Yelluw"),
            ("software development", "I need software development services"),
            ("digital marketing", "I'm a business owner and want help driving growth"),
            ("content production", "I need quality content produced"),
        )

    ATTRS = {"class": "form-control"}

    inquiry_type = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES)
    name = forms.CharField(widget=forms.TextInput(attrs=ATTRS), max_length=140)
    email = forms.EmailField(widget=forms.EmailInput(attrs=ATTRS))
    company = forms.CharField(widget=forms.TextInput(attrs=ATTRS), max_length=140)
    phone = forms.CharField(widget=forms.TextInput(attrs=ATTRS), max_length=40)
    message = forms.CharField(widget=forms.Textarea(attrs=ATTRS))
