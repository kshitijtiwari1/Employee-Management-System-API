from django.urls import path
from Employee import views

urlpatterns=[
    path('leave-applications/',views.LeaveList.as_view()), # url path for leave application list
    path('leave-application/create/',views.LeaveCreate.as_view()), # url path for the create leave application
    path('leave-application/detail/<int:pk>', views.LeaveApplicationDetail.as_view()), # url path for the detail of a particular leave application
] 