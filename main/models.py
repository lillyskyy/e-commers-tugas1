

from django.db import models
import uuid

class AdditionalEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    era = models.CharField(max_length=50)
    time = models.DateField(auto_now_add=True)
    condition = models.TextField()
    stock = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name