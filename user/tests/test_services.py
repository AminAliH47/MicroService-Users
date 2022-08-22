from django_grpc_framework.test import RPCTestCase
from user.models import User
from user_proto import user_pb2_grpc
from user_proto import user_pb2


class TestUserServices(RPCTestCase):
    def setUp(self):
        self.user1 = User.objects.create(  # create our first test case
            username="test1",
            first_name="test1 first",
            last_name="test1 last",
            email="test1@test.com",
            password="Test12345",
        )
        self.user2 = User.objects.create(  # create our second test case
            username="test2",
            first_name="test2 first",
            last_name="test2 last",
            email="test2@test.com",
            password="Test12345",
        )
        self.channel = self.channel_class()

    def test_create_user(self):
        """
        Checks user created successfully with gRPC or not
        """
        stub = user_pb2_grpc.UserControllerStub(self.channel)
        response = stub.Create(  # Create our testcase
            user_pb2.User(
                username="test",
                first_name="test first",
                last_name="test last",
                email="test@test.com",
                password="Test12345",
            )
        )
        self.assertEqual(response.username, "test")
        self.assertEqual(response.first_name, "test first")
        self.assertEqual(response.last_name, "test last")
        self.assertEqual(response.email, "test@test.com")
        self.assertEqual(response.password, "Test12345")
        self.assertEqual(User.objects.count(), 3)

    def test_user_lists(self):
        """
        Checks length of users list count with gRPC
        """
        stub = user_pb2_grpc.UserControllerStub(self.channel)
        users_list = list(stub.List(user_pb2.UserListRequest()))
        self.assertEqual(len(users_list), 2)

    def test_update_user(self):
        """
        Checks user updated successfully with gRPC or not
        """
        stub = user_pb2_grpc.UserControllerStub(self.channel)
        response = stub.Update(  # Update our testcase
            user_pb2.User(
                id=self.user1.id,
                username="test",
                first_name="test first",
                last_name="test last",
                email="test@test.com",
                password="Test12345",
            )
        )
        self.assertEqual(response.username, "test")
        self.assertEqual(response.first_name, "test first")
        self.assertEqual(response.last_name, "test last")
        self.assertEqual(response.email, "test@test.com")
        self.assertEqual(response.password, "Test12345")

    def test_delete_user(self):
        """
        Checks user deleted successfully with gRPC or not
        """
        stub = user_pb2_grpc.UserControllerStub(self.channel)
        stub.Delete(  # Update our testcase
            user_pb2.User(
                id=self.user1.id,
            )
        )
        self.assertEqual(User.objects.count(), 1)
