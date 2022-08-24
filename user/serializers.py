from django_grpc_framework import proto_serializers as p_serializer
from common.auth import authenticate
from user.models import User
from user_proto import user_pb2
from rest_framework import serializers


class UserProtoSerializer(p_serializer.ModelProtoSerializer):
    """
    Create proto serializer for User model
    """

    class Meta:
        model = User
        proto_class = user_pb2.User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_authenticated",
            "is_active",
        )


class IsUserExistsSerializer(p_serializer.ProtoSerializer):
    """
    Serialize user id and checks user exists or not
    """
    id = serializers.IntegerField(required=True)

    def is_valid(self, raise_exception=False):
        super(IsUserExistsSerializer, self).is_valid()

        pk = self.message.id

        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exists", code=404)

        self.message.id = user.id
        self.message.username = user.username
        self.message.first_name = user.first_name
        self.message.last_name = user.last_name
        self.message.email = user.email
        self.message.password = user.password
        self.message.is_authenticated = user.is_authenticated

    class Meta:
        proto_class = user_pb2.User


class UserLoginSerializer(p_serializer.ProtoSerializer):
    """
    Serialize user username and password
    and checks is user exists for login
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def is_valid(self, raise_exception=False):
        super(UserLoginSerializer, self).is_valid()

        username = self.message.username
        password = self.message.password

        user = authenticate(username, password)

        self.message.id = user.id
        self.message.username = user.username
        self.message.first_name = user.first_name
        self.message.last_name = user.last_name
        self.message.email = user.email
        self.message.password = user.password
        self.message.is_authenticated = user.is_authenticated

    class Meta:
        proto_class = user_pb2.User
