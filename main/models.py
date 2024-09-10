

from django.db import models

class VintageEntry(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    era = models.CharField(max_length=50)  
    condition = models.CharField(max_length=50)  
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name