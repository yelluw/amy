from django import forms


class DripSubscriberForm(forms.Form):
    """
    Form for drip content subscribers
    """

    ATTRS = {"class": "form-control input-lg"}

    email = forms.EmailField(widget=forms.EmailInput(attrs=ATTRS))
    funnel_entry_point = forms.CharField(widget=forms.HiddenInput())


class CreateDripSubscriberListForm(forms.Form):
    """
    Form to create new drip subscriber lists
    """

    ATTRS = {"class": "form-control"}

    name = forms.CharField(widget=forms.TextInput(attrs=ATTRS))


class UpdateDripSubscriberListForm(forms.Form):
    """
    Form to update drip subscriber lists
    """

    ATTRS = {"class": "form-control"}

    name = forms.CharField(widget=forms.TextInput(attrs=ATTRS))
    drip_subscriber_list_id = forms.CharField(widget=forms.HiddenInput())


class EmailSingleDripSubscriberForm(forms.Form):
    """
    Form to email a single drip subscriber
    """

    ATTRS = {"class": "form-control"}

    email = forms.EmailField(widget=forms.EmailInput(attrs=ATTRS))
    subject = forms.CharField(widget=forms.TextInput(attrs=ATTRS))
    message = forms.CharField(widget=forms.Textarea(attrs=ATTRS))
