from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        content = {
            'user': str(self.request.user),
            'auth': str(self.request.auth),
        }
        return Response(content)
