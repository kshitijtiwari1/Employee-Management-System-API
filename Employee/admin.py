from django.contrib import admin
from  Employee.models import LeaveApplicationModel

# Adding the LeaveApplicationModel to the admin page
admin.site.register(LeaveApplicationModel)