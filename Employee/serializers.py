from rest_framework import serializers
from Employee.models import LeaveApplicationModel


# Serializer for Creating Leave Application 
class LeaveApplicationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaveApplicationModel 
        exclude = ['employee','status']

    # create funtion for leave application
    def create(self, validated_data):

        # getting the current employee id
        employee = self.context.get('employee')
        
        # Creating the new leave application and sotres in LeaveApplicationModel
        return LeaveApplicationModel.objects.create(**validated_data, employee=employee)


# Serializer for List Of Applied Leave
class LeaveApplicationsListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = LeaveApplicationModel
        exclude = ['id', 'employee']