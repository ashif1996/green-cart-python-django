from django import forms

from store.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'district', 'state', 'country', 'postcode']
        widgets = {'street': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Popular Place like Restaurant, Religious Site, etc.'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State or Province'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'postcode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'postcode'})}
