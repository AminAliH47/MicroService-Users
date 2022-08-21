from django.contrib.auth.hashers import make_password
from django_grpc_framework import proto_serializers as p_serializer
from user.models import User
from user_proto import user_pb2


class UserProtoSerializer(p_serializer.ModelProtoSerializer):
    """
    Create proto serializer for User model
    """
    def get_password(self, obj):
        """
        Hash entered password and then save in Database
        """
        return make_password(obj.password)

    class Meta:
        model = User
        proto_class = user_pb2.User
        fields = (
            'id', 'username',
            'first_name', 'last_name',
            'email', 'password',
        )
