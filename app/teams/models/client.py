from django.db import models

from utils.models import BaseModel
from .team import Team


class Client(BaseModel):
    company_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
