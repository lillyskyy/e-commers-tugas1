from django.forms import ModelForm
from main.models import AdditionalEntry

class AdditionalEntryForm(ModelForm):
    class Meta:
        model = AdditionalEntry
        fields = ["era", "condition", "stock", "name", "price", "description"]