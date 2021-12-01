from django.db import models

from utils.models import BaseModel
from .client import Client


class Website(BaseModel):
    name = models.CharField(max_length=100)
    domain = models.URLField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("domain", "client")
