from django.db import models

# importing user model
from django.contrib.auth.models import User

# Creating Employeemodel
class EmployeeModel(models.Model):

    # model fields
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=50,null=False)
    contact_number =models.IntegerField()
    emergency_contact_number = models.IntegerField()
    address = models.TextField()
    postion = models.CharField(max_length=250)
    dob = models.DateField()
    martial_status = models.BooleanField(default=False)
    blood_group = models.CharField(max_length=10)
    job_title = models.CharField(max_length=250)
    work_location = models.CharField(max_length=250)
    date_of_joining = models.DateField(auto_now=True)
    reporting_to = models.CharField(max_length=250)
    linked_in = models.URLField(max_length=250)
    profile_picture = models.ImageField(upload_to='media/profile', blank=True)
    email = models.EmailField(unique=True,null=False)
    password = models.CharField(max_length=100)



    def _unicode_(self):
        return self.employee_name
    
    def image_img(self):
        if self.profile_picture:
            return u'<img src="%s"/>'%self.profile_picture.url
        else:
            return '(profile_picture)'

    def __str__(self):
        return '{}'.format(self.employee_name)