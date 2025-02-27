from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def show_my_reports(request):
    reports = Report.objects.filter(user=request.user)
    serializer = ReportSerializer(reports, many=True)
    return Response({"reports": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_report(request):
    if request.user.id != int(request.data['user']):
        return Response({"message":"Not the same authorized user"},status=status.HTTP_401_UNAUTHORIZED)
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Report submitted successfully", "report": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_report(request,report_id):
    if request.user.id != int(request.data['user']):
        return Response({"message":"Not the same authorized user"},status=status.HTTP_401_UNAUTHORIZED)
    try:
        report = Report.objects.get(pk = report_id)
        if report.user_id != request.user.id:
            return Response({"message":"Not the same authorized user"},status=status.HTTP_401_UNAUTHORIZED)
    except Report.DoesNotExist:
        return Response({"message": "Report not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ReportSerializer(report,data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Report updated successfully", "report": serializer.data}, status=status.HTTP_200_OK)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_report(request,report_id):
    try:
        report = Report.objects.get(pk = report_id)
        if report.user_id != request.user.id:
            return Response({"message":"Not the same authorized user"},status=status.HTTP_401_UNAUTHORIZED)
    except Report.DoesNotExist:
        return Response({"message": "Report not found"}, status=status.HTTP_404_NOT_FOUND)
    
    report.delete()
    return Response({"message": "Report deleted successfully"}, status=status.HTTP_200_OK)
