from django.db import models

from utils.models import BaseModel


class Team(BaseModel):
    name = models.CharField(max_length=100)
