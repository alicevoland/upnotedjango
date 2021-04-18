import datetime
from contextvars import Token

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import Note
from api.serializers import NoteSerializer


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class NoteViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        return self.queryset.filter(user__exact=self.request.user)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in User."""
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_at=datetime.datetime.now())


class TestView(APIView):

    def get(self, request):
        print(request.user)
        return Response({
            "is_authenticated": request.user.is_authenticated
        })

