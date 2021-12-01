from django.db import models

from utils.models import BaseModel
from .website import Website


class WebPage(BaseModel):
    url = models.URLField()
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("url", "website")
