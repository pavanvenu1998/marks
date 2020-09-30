from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from .models import student,Employee
from marks.serializers import studentSerializer,EmployeeSerializer

from rest_framework.parsers import JSONParser
import json


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def students_list(request):
    """
    List all code  service, or create a new  service.
    """
    if request.method == 'GET':
        marks1 = student.objects.all()
        serializer = studentSerializer(marks1, many=True)
        return Response({"students_list_marks": serializer.data, })

    elif request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "succesfully updated the student details", "student_id: ": "#collegename-" + str(serializer.data['id'])},
                status=status.HTTP_201_CREATED)

        return Response({"status": "not posted", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def students(request, id):

    try:
        status_flag = student.objects.get(id=id)
    except status_flag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        service1 = student.objects.get(id=id)
        serializer = studentSerializer(service1)
        return Response({"student": serializer.data})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def employees(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        return Response({"Employee": serializer.data},)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "succesfully updated the post", "company_id: ": "#companyname-" + str(serializer.data['id'])},
                status=status.HTTP_201_CREATED)

        return Response({"status": "not posted", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


