from typing import cast, Optional
from django.db.models.query import QuerySet

from teams.models import Client


class ClientRepository:
    @staticmethod
    def all() -> QuerySet:
        return Client.objects.all()

    @staticmethod
    def save(client: Client) -> Client:
        client.save()
        return client

    @staticmethod
    def get(clinet_id: int) -> Optional[Client]:
        try:
            client = Client.objects.get(id=clinet_id)
            return cast(Client, client)
        except Client.DoesNotExist:
            return None

    @staticmethod
    def delete(clinet_id: int):
        if client := ClientRepository.get(clinet_id):
            client.delete()

        return cast(Client, client)

    @staticmethod
    def is_dirty(client: Client) -> bool:
        return cast(bool, client.is_dirty())
