
from rest_framework import serializers
from Admin.models import EmployeeModel
from Employee.models import LeaveApplicationModel
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

### EMPLOYEE PAGE###
# Create Employee Serializer
class EmployeeCreateSerializer(serializers.ModelSerializer):

    # field for profile picture 
    profile_picture = serializers.ImageField(max_length=None, use_url=True, required=False)
    
    class Meta:
        model = EmployeeModel
        exclude = ['employee']

    # Create function    
    def create(self, validated_data):

        # validating the data
        employee = User(email=self.validated_data['email'], username=self.validated_data['email'])
        password =  self.validated_data['password']
        
        # password converting into hashed format
        employee.set_password(password)
        
        # employee email and username and password is saving in User table
        employee.save()
        
        # creating the new employee and stores in Employee table
        return EmployeeModel.objects.create(**validated_data,employee=employee)


# Employee Lsit Serializer
class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'employee_name', 'contact_number', 'email', 'postion', 'reporting_to', 'work_location'] 
    
class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        exclude = ['employee']

# Employee Delete Serializer
class EmployeeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'


##### LEAVE APPLICATIONS ######
# Leave Application List
class LeaveApplicationListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = LeaveApplicationModel
        fields = ['id','employee','apply_date','nature_of_leave','first_day','last_day','number_of_days','status']

    # Displaying Employee username insted of Employee id
    def to_representation(self, instance):
        rep = super(LeaveApplicationListSerializer, self).to_representation(instance)
        rep['employee'] = instance.employee.username
        return rep

# Leave Application Status Update
class LeaveApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplicationModel
        fields = ['status']