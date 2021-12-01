from rest_framework.serializers import Serializer, CharField


class SendUsMessageSerializer(Serializer):
    full_name = CharField()
    phone_number = CharField()
    message = CharField()
