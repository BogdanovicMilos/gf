from rest_framework.serializers import Serializer, IntegerField, CharField, URLField, PrimaryKeyRelatedField


class WebsiteSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=254)
    domain = URLField()
    client = PrimaryKeyRelatedField(read_only=True)
