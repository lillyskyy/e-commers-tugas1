

from django.db import models
import uuid
from django.contrib.auth.models import User

class AdditionalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.CharField(max_length=50)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    # name = models.CharField(max_length=200)
    # price = models.IntegerField(default=0)
    # description = models.TextField()

    def __str__(self):
        return self.name