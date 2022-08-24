import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from user.models import User
from user.serializers import (
    UserProtoSerializer,
    UserLoginSerializer,
    IsUserExistsSerializer,
)


class UserService(Service):
    def List(self, request, context):
        """
        Returns list of all users
        """
        users = User.objects.all()
        serializer = UserProtoSerializer(users, many=True)
        for message in serializer.message:
            yield message

    def Create(self, request, context):
        """
        check if serializer is valid then Create user
        """
        serializer = UserProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        """
        Check if user object is exists returns object
        else raise  User does not exists exception
        """
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            self.context.abort(
                grpc.StatusCode.NOT_FOUND, f"User with id {pk} was not found!"
            )

    def Retrieve(self, request, context):
        """
        Returns the user whose ID is equal to the PK (Primary Key)
        """
        user = self.get_object(request.id)
        serializer = UserProtoSerializer(user)

        return serializer.message

    def Update(self, request, context):
        """
        Update user data whose ID is equal to the PK (Primary Key)
        """
        user = self.get_object(request.id)
        serializer = UserProtoSerializer(user, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.message

    def Delete(self, request, context):
        """
        Delete user whose ID is equal to the PK (Primary Key)
        """
        user = self.get_object(request.id)
        user.delete()

        return empty_pb2.Empty()

    def IsUserExists(self, request, context):
        """
        checks user exists or not

        :returns: User object
        """
        serializer = IsUserExistsSerializer(message=request)
        serializer.is_valid(raise_exception=True)

        return serializer.message

    def Login(self, request, context):
        """
        if user is valid return user object to Signin and authentication
        in Gateway Service

        :returns: User object
        """
        serializer = UserLoginSerializer(message=request)
        serializer.is_valid(raise_exception=True)

        return serializer.message
