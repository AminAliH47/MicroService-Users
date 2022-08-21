import grpc
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from user_proto.user_pb2 import UserListRequest
from user_proto.user_pb2_grpc import UserControllerStub

channel = grpc.insecure_channel('localhost:50051')
stub = UserControllerStub(channel)


# class UsersView(APIView):
#     def get(self, reqeust):
#         print(type(stub.List(UserListRequest())))
#         return Response({"message": "hello"})
#
#     def post(self, request):

