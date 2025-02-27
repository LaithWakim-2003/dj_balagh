from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Governorate,City
from .serializers import GovernorateSerializer,CitySerializer
from django.shortcuts import get_object_or_404



@api_view(['GET'])
def get_governorates(request):
    governorates = Governorate.objects.all()
    serializer = GovernorateSerializer(governorates, many = True)
    return Response({'governorates':serializer.data},status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_governorate(request):
    if request.user.user_type not in ['admin']:
        return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    serializer = GovernorateSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Governorate created successfully","governorate":serializer.data},status=status.HTTP_201_CREATED)
    return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_governorate(request, governorate_id):
    if request.user.user_type not in ['admin']:
        return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        governorate = Governorate.objects.get(pk=governorate_id)
    except Governorate.DoesNotExist:
        return Response({"message": "Governorate not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = GovernorateSerializer(governorate, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Governorate updated successfully", "governorate": serializer.data}, status=status.HTTP_200_OK)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_governorate(request, governorate_id):
    if request.user.user_type not in ['admin']:
        return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        governorate = Governorate.objects.get(pk=governorate_id)
    except Governorate.DoesNotExist:
        return Response({"message": "Governorate not found"}, status=status.HTTP_404_NOT_FOUND)

    governorate.delete()
    return Response({"message": "Governorate deleted successfully"}, status=status.HTTP_200_OK)





@api_view(['GET'])
def get_cities(request,governorate_id):
    cities = City.objects.filter(governorate = governorate_id)
    serializer = CitySerializer(cities,many = True)
    return Response({'cities':serializer.data},status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_city(request):
    if request.user.user_type not in ['admin']:
        return Response({"message":"Not Authorized"},status=status.HTTP_401_UNAUTHORIZED)
    serializer = CitySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"City created successfully","city":serializer.data},status=status.HTTP_201_CREATED)
    return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_city(request, city_id):
    if request.user.user_type not in ['admin']:
        return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        city = City.objects.get(pk=city_id)
    except City.DoesNotExist:
        return Response({"message": "City not found"}, status=status.HTTP_404_NOT_FOUND)
    
    poped_data = request.data.copy()
    poped_data.pop('governorate',None)
    
    serializer = CitySerializer(city, data=poped_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "City updated successfully", "city": serializer.data}, status=status.HTTP_200_OK)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_city(request, city_id):
    if request.user.user_type not in ['admin']:
        return Response({"message": "Not Authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        city = City.objects.get(pk=city_id)
    except City.DoesNotExist:
        return Response({"message": "City not found"}, status=status.HTTP_404_NOT_FOUND)

    city.delete()
    return Response({"message": "City deleted successfully"}, status=status.HTTP_200_OK)
