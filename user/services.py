import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from user.models import User
from user.serializers import UserProtoSerializer


class UserService(Service):
    def List(self, request, context):
        users = User.objects.all()
        serializer = UserProtoSerializer(users, many=True)
        for message in serializer.message:
            yield message

    def Create(self, request, context):
        serializer = UserProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, f'User with id:{pk} was not found!')

    def Retrieve(self, request, context):
        user = self.get_object(request.id)
        serializer = UserProtoSerializer(user)
        return serializer.message

    def Update(self, request, context):
        user = self.get_object(request.id)
        serializer = UserProtoSerializer(user, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Delete(self, request, context):
        user = self.get_object(request.id)
        user.delete()
        return empty_pb2.Empty()
