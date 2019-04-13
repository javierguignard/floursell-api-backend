from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

class GetMyUserType(viewsets.ModelViewSet):
    """
        Return actual user data:

    """
    def __str__(self):
        return 'My data'

    http_method_names = ['get']

    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)


    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return User.objects.filter(id=user.id)
        else:
            return User.objects.none()
#
# class GetMyUserType(APIView):
#     """
#     """
#     authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
#
#     def get(self, request, format=None):
#         """
#         Return serialized user.
#         """
#         return Response(UserSerializer(request.user))