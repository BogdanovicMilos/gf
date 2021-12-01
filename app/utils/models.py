from django.db import models


class BaseModel(models.Model):
    """
    Base model that includes default created / updated timestamps.
    """

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=False, null=True)

    class Meta:
        abstract = True
