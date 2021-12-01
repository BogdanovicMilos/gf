from rest_framework.serializers import Serializer, CharField


class ScheduleCallSerializer(Serializer):
    full_name = CharField()
    phone_number = CharField()
