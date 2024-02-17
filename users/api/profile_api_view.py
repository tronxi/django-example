from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.persistence.profile_serializer import ProfileSerializer


class ProfileAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated()]

    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user, many=False)
        return Response(serializer.data)
