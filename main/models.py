

from django.db import models
import uuid

class AdditionalEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    era = models.CharField(max_length=50)
    time = models.DateField(auto_now_add=True)
    condition = models.TextField()
    stock = models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    # era = models.CharField(max_length=50)  
    # condition = models.CharField(max_length=50)  
    # stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name