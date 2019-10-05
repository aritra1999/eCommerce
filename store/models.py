from django.db import models

class Store(models.Model):
    owner = models.CharField(max_length=120)
    store_name = models.CharField(max_length=120)
    store_address = models.CharField(max_length=120)

    def __str__(self):
        return self.store_name
