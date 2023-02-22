from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from Admin import views

urlpatterns=[

    # Employee related urls
    path('employee-create/', views.EmployeeCreate.as_view()), # url path for the create 
    path('employee-list/', views.EmployeeList.as_view()), # url path for the employee list
    path('employee-detail/<int:pk>/', views.EmployeeDetail.as_view()), # url path for the detail for the particular employee
    path('employee-update/<int:pk>/', views.EmployeeUpdate.as_view()), # url path for the edit/update for the particular employee
    path('employee-delete/<int:pk>/', views.EmployeeDelete.as_view()), # url path for delete an employee

    # Leave Realted urls
    path('leave-application-list/', views.LeaveApplicationList.as_view()), # url path for the all leave applications
    path('leave-application-details/<int:pk>/', views.LeaveApplicationDetail.as_view()), # url path for the particular leave details
    path('leave-application-update/<int:pk>/', views.LeaveApplicationUpdate.as_view()), # url path for the change the status of the particular leave application
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
