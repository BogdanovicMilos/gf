from rest_framework.serializers import Serializer, IntegerField, URLField, PrimaryKeyRelatedField


class WebPageSerializer(Serializer):
    id = IntegerField(read_only=True)
    url = URLField()
    website = PrimaryKeyRelatedField(read_only=True)
