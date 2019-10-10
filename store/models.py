from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Store(models.Model):
    # owner = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120,)
    country = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return self.store_name
