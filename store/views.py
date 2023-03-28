from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from .forms import AddressForm
from .models import *


def home(request):
    return render(request, 'home.html', {})


def store(request):
    items = Product.objects.filter(is_active=True)
    return render(request, 'store.html', {'items': items})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'add_address.html', {'form': form})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            user = request.user
            street = form.cleaned_data['street']
            district = form.cleaned_data['district']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            postcode = form.cleaned_data['postcode']
            reg = Address(user=user, street=street, district=district, state=state, country=country, postcode=postcode)
            reg.save()
            messages.success(request, "New Address Added Successfully.")
        return redirect('profile')


@login_required(login_url='login')
def remove_address(request, id):
    a = get_object_or_404(Address, user=request.user, id=id)
    a.delete()
    messages.success(request, "Address removed.")
    return redirect('profile')
