from rest_framework.serializers import Serializer, IntegerField, CharField


class TeamSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=100)
