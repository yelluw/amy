from django import forms


class DripSubscriberForm(forms.Form):
    """
    Form for drip content subscribers
    """

    ATTRS = {"class": "form-control input-lg"}

    email = forms.EmailField(widget=forms.EmailInput(attrs=ATTRS))
    funnel_entry_point = forms.CharField(widget=forms.HiddenInput())
