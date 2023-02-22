from django.contrib import admin

# importing the userdefined model 'EmployeeModel' from App_admin 
from Admin.models import EmployeeModel


# Adding the Employee model table to the admin page
admin.site.register(EmployeeModel)