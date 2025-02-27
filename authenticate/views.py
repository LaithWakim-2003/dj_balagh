from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer,LoginSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def register(request):
    if request.data['user_type'] not in ['manager','user']:
        return Response({"message":"invalid user type"},status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(phone_number = request.data['phone_number'])
        user.set_password(request.data['password'])
        # passing validation: (No SMS API available)
        user.is_active = True
        user.save()
        return Response({'message':'User created successfully','user':serializer.data},status=status.HTTP_201_CREATED)
    return Response({"error": serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data = request.data)
    if serializer.is_valid():
        user = get_object_or_404(User,phone_number = request.data['phone_number'])
        if not user.check_password(request.data['password']):
            return Response({"message":"Invalid phone number or password"},status=status.HTTP_400_BAD_REQUEST)
        if user.is_active == False:
            return Response({"message":"User is not activated"},status=status.HTTP_400_BAD_REQUEST)
        token,created = Token.objects.get_or_create(user = user)
        user_serializer = UserSerializer(instance = user)
        return Response({"message":"User logged-in successfully",'token':token.key,'user':user_serializer.data},status=status.HTTP_200_OK)
    return Response({"error": serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    user = request.user
    token = get_object_or_404(Token,user = user)
    token.delete()
    return Response({"message":"User logged-out successfully"},status=status.HTTP_200_OK)