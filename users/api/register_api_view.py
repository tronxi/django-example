from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.persistence.custom_user import CustomUser
from users.persistence.register_serializer import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterSerializer
