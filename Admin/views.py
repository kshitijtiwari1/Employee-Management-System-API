from django.shortcuts import render
from Admin.models import EmployeeModel
from Employee.models import LeaveApplicationModel

from rest_framework  import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import OrderingFilter
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EmployeeCreateSerializer,EmployeeListSerializer,EmployeeDeleteSerializer,EmployeeUpdateSerializer
from .serializers import  LeaveApplicationListSerializer, LeaveApplicationUpdateSerializer

#**************** EMPLOYEE PAGE ****************************
## Create Emmployee
class EmployeeCreate(generics.CreateAPIView):

    queryset = EmployeeModel.objects.all()
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = EmployeeCreateSerializer

# Employee ListView
class EmployeeList(generics.ListAPIView):

    queryset = EmployeeModel.objects.all()
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = EmployeeListSerializer
    
    # filtering and ordering 
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['id', 'employee_name', 'work_location']
    ordering_fields = ['id', 'employee_name', 'work_location']
    

# Employee Detail View
class EmployeeDetail(generics.RetrieveAPIView):

    queryset = EmployeeModel.objects.all()
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    serializer_class = EmployeeCreateSerializer


# Employee Update View
class EmployeeUpdate(generics.UpdateAPIView):

    queryset = EmployeeModel.objects.all()
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    serializer_class = EmployeeUpdateSerializer

# Employee Delete
class EmployeeDelete(generics.DestroyAPIView):

    queryset = EmployeeModel.objects.all()
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    serializer_class = EmployeeDeleteSerializer


#************ LEAVE PAGE ********************************************

# Leave Applications List
class LeaveApplicationList(generics.ListAPIView):

    queryset = LeaveApplicationModel.objects.all()
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = LeaveApplicationListSerializer
    
    # filtering and ordering
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['status']
    ordering_fields = ['employee', 'status',]
   

# Leave Application detail
class LeaveApplicationDetail(generics.RetrieveAPIView):

    queryset = LeaveApplicationModel.objects.all()
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = LeaveApplicationListSerializer

# Leave Status update
class LeaveApplicationUpdate(generics.UpdateAPIView):

    queryset = LeaveApplicationModel.objects.all()
    
    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser,DjangoModelPermissions]
    
    serializer_class = LeaveApplicationUpdateSerializer