from rest_framework.serializers import Serializer, IntegerField, EmailField, PrimaryKeyRelatedField


class UserSerializer(Serializer):
    id = IntegerField(read_only=True)
    email = EmailField(required=False, allow_null=False)
    team = PrimaryKeyRelatedField(read_only=True)
