from typing import cast, Optional
from django.db.models.query import QuerySet

from teams.models import WebPage


class WebPageRepository:
    @staticmethod
    def all() -> QuerySet:
        return WebPage.objects.all()

    @staticmethod
    def save(webpage: WebPage) -> WebPage:
        webpage.save()
        return webpage

    @staticmethod
    def get(webpage_id: int) -> Optional[WebPage]:
        try:
            webpage = WebPage.objects.get(id=webpage_id)
            return cast(WebPage, webpage)
        except WebPage.DoesNotExist:
            return None

    @staticmethod
    def delete(webpage_id: int):
        if webpage := WebPageRepository.get(webpage_id):
            webpage.delete()

        return cast(WebPage, webpage)

    @staticmethod
    def is_dirty(webpage: WebPage) -> bool:
        return cast(bool, webpage.is_dirty())
