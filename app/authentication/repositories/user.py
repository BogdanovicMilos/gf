from typing import cast
from authentication.models import User


class UserRepository:
    @staticmethod
    def all():
        return User.objects.all()

    @staticmethod
    def save(user: User):
        user.save()
        return user

    @staticmethod
    def get(user_id: int):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def delete(user_id: int):
        if user := UserRepository.get(user_id):
            user.delete()

        return cast(User, user)

    @staticmethod
    def is_dirty(user: User):
        return user.is_dirty()
