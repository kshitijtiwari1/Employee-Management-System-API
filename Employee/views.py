from django.shortcuts import render
from Employee.models import LeaveApplicationModel

from rest_framework  import generics
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import LeaveApplicationCreateSerializer, LeaveApplicationsListSerializer


# Create Leave Application
class LeaveCreate(generics.CreateAPIView):

    queryset = LeaveApplicationModel.objects.all()

    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

    serializer_class = LeaveApplicationCreateSerializer

    # create function 
    def create(self, request, *args, **kwargs):
        
        # getting current logined user
        employee = request.user

        # Checking for the non super user
        if employee.is_superuser == 0:

            # over riding function
            serializer = LeaveApplicationCreateSerializer(data = request.data, context={'employee': employee})

            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data= serializer.errors)
        
        # Error message for the super user
        else:
            return Response({'Error-Message':"You Don't have permission to access this Page"})

# List of Leave Application for the Current user
class LeaveList(generics.ListAPIView):

    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]  
    
    # filtering, searching and ordering 
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    ordering_fields = ['apply_date','number_of_days','status']
    search_fields = ['status']
    filter_fields = ['status']
    
    serializer_class = LeaveApplicationsListSerializer

    # get query function for getting the current user detail and filtering the status
    def get_queryset(self):

        # taking the current user id
        employee = self.request.user
        
        # filter out the all leave applications that the current user applied
        queryset = LeaveApplicationModel.objects.filter(employee_id=employee.id)
        return queryset

# Leave Application detail view
class LeaveApplicationDetail(generics.RetrieveAPIView):
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]  
    
    serializer_class = LeaveApplicationsListSerializer

    # get query function for getting the current user detail and filtering the status
    def get_queryset(self):

        # taking the current user id
        employee = self.request.user
        
        # filter out the all leave applications that the current user applied
        queryset = LeaveApplicationModel.objects.filter(employee_id=employee.id)
        return queryset