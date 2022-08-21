import grpc
from user_proto import user_pb2, user_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = user_pb2_grpc.UserControllerStub(channel)
    # print('----- Create -----')
    # response = stub.Create(user_pb2.User(username="test", first_name="Test", last_name="Mz",
    #                                      email="test@test2.com", password="Admin123456"))
    # print(response, end='')
    # print('----- List -----')
    # for user in stub.List(user_pb2.UserListRequest()):
    #     print(user, end='')
    print('----- Retrieve -----')
    response = stub.Retrieve(user_pb2.UserRetrieveRequest(id=3))
    print(response, end='')
    # print('----- Update -----')
    # response = stub.Update(user_pb2.User(id=response.id, username="aminali", first_name="AminAli", last_name="Mz",
    #                                      email="Hello@test.com", password="Admin123456"))
    # print(response, end='')
    # print('----- Delete -----')
    # stub.Delete(user_pb2.User(id=2))
