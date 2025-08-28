from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from accounts.serializers import UserSerializer, LoginSerializer, CustomerRegistrationSerializer, \
    AgentRegistrationSerializer

# Create your views here.

User = get_user_model()


class CustomAuthTokenView(ObtainAuthToken):
    """ This view is to retrieve a token for authentication"""

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not email or not password:
            return Response(
                {'error': 'Please provide email and password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )

        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'id': user.id,
                'name': f'{user.first_name} {user.last_name}',
                'email': user.email,
                'token': token.key
            },
            status=status.HTTP_200_OK
        )


class AccountListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_agent']
    permission_classes = [IsAuthenticated, IsAdminUser]


class CustomerRegistrationAPIView(generics.CreateAPIView):
    serializer_class = CustomerRegistrationSerializer


class AgentRegistrationAPIView(generics.CreateAPIView):
    serializer_class = AgentRegistrationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only Admins will be allowed to register new Agents


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        login(request, user)

        return Response({
            'token': token.key,
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }, status=status.HTTP_200_OK)
