from django.shortcuts import render, redirect
from main.forms import AdditionalEntryForm
from main.models import AdditionalEntry
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    additional_entries = AdditionalEntry.objects.all()

    context = {
        'name': 'Vintage Flower Dress',
        'price': 'Rp 250.000',
        'description': 'The Vintage Flower Dress is a timeless piece featuring a classic floral print.',
        'additional_entries': additional_entries
        # 'era': '80s',
        # 'condition': '60% ',
        # 'stock': '5'
    }
    return render(request, 'main.html', context)

def create_additional_entry(request):
    form = AdditionalEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_additional_entry.html", context)

def show_xml(request):
    data = AdditionalEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")