from rest_framework.serializers import Serializer, IntegerField, CharField, PrimaryKeyRelatedField


class ClientSerializer(Serializer):
    id = IntegerField(read_only=True)
    company_name = CharField(max_length=254)
    team = PrimaryKeyRelatedField(read_only=True)
