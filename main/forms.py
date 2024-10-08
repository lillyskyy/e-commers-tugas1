from django.forms import ModelForm
from main.models import AdditionalEntry

from django.utils.html import strip_tags

class AdditionalEntryForm(ModelForm):
    class Meta:
        model = AdditionalEntry
        fields = ['product', 'description', 'stock', 'price']

    def clean_product(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)