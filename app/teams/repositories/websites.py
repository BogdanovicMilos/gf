from typing import cast, Optional
from django.db.models.query import QuerySet

from teams.models import Website


class WebsiteRepository:
    @staticmethod
    def all() -> QuerySet:
        return Website.objects.all()

    @staticmethod
    def save(website: Website) -> Website:
        website.save()
        return website

    @staticmethod
    def get(website_id: int) -> Optional[Website]:
        try:
            website = Website.objects.get(id=website_id)
            return cast(Website, website)
        except Website.DoesNotExist:
            return None

    @staticmethod
    def delete(website_id: int):
        if website := WebsiteRepository.get(website_id):
            website.delete()

        return cast(Website, website)

    @staticmethod
    def is_dirty(website: Website) -> bool:
        return cast(bool, website.is_dirty())
