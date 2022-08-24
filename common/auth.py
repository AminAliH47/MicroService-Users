from rest_framework.exceptions import ValidationError
from user.models import User


def authenticate(username: str, password: str):
    """
    It checks if there is a user with
    the received username and password in the database

    :params username: User string username
    :params password: User string raw_password (password without hash)
    :returns: User Object
    """

    try:
        user = User.objects.get(username=username)

    except User.DoesNotExist:
        raise ValidationError("No user found with this information.", code=404)

    is_password_correct = user.check_password(password)
    if not is_password_correct:
        raise ValidationError("User Password is incorrect!", code=403)

    return user
