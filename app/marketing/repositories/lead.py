from typing import cast, Optional
from django.db.models.query import QuerySet

from marketing.models import Lead


class LeadRepository:
    @staticmethod
    def all() -> QuerySet:
        return Lead.objects.all()

    @staticmethod
    def save(lead: Lead) -> Lead:
        lead.save()
        return lead

    @staticmethod
    def get(lead_id: int) -> Optional[Lead]:
        try:
            lead = Lead.objects.get(id=lead_id)
            return cast(Lead, lead)
        except Lead.DoesNotExist:
            return None

    @staticmethod
    def delete(lead_id: int):
        if lead := LeadRepository.get(lead_id):
            lead.delete()

        return cast(Lead, lead)

    @staticmethod
    def is_dirty(lead: Lead) -> bool:
        return cast(bool, lead.is_dirty())
