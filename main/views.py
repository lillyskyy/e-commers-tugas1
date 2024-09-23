from django.shortcuts import render, redirect
from main.forms import AdditionalEntryForm
from main.models import AdditionalEntry
from django.http import HttpResponse
from django.core import serializers
from django.forms import ModelForm

class AdditionalEntryForm(ModelForm):
    class Meta:
        model = AdditionalEntry
        fields = ["product", "description", "stock"]
        
def show_main(request):
    additional_entries = AdditionalEntry.objects.all()

    context = {
        'name': 'Ananda Dwi Hanifa',
        'npm': '2306165572',
        'class': 'PBP A',
        'additional_entries': additional_entries

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

def show_json(request):
    data = AdditionalEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = AdditionalEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = AdditionalEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")