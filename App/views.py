from django.shortcuts import render
from django.contrib.auth import login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

# index page
class IndexView(APIView):

    # Authentication classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    
    # permission classes
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        # getting the current logined user
        user = request.user
        
        # checking for the logined user is super user or not 
        if user.is_superuser == 1:

            # content for super user
            content = {
                'PROJECT NAME':'EMPLOYEE MANAGMENT SYSTEM',
                '---------------':'-----------------------------',
                'LOGIN-USER' : str(user),
                'LOGIN-USER-PROFILE' : 'http://127.0.0.1:8000/profile/',
                '::::::::::::::':'::::::::::::::::::',
                'CREATE EMPLOYEE' : 'http://127.0.0.1:8000/accounts/manager/employee-create/',
                'EMPLOYEE LIST':'http://127.0.0.1:8000/accounts/manager/employee-list/',
                'EMPLOYEE DETAILS' : 'http://127.0.0.1:8000/accounts/manager/employee-detail/<id>/',
                '.......................':'...................................',
                'LEAVE APPLICATION LIST' : 'http://127.0.0.1:8000/accounts/manager/leave-application-list/',
                'LEAVE APPLICATION APPROVAL':'http://127.0.0.1:8000/accounts/manager/leave-application-details/<id>/',
                'LEAVE APPLICATION APPROVAL':'http://127.0.0.1:8000/accounts/manager/leave-application-update/<id>/',
                '.......................':'...................................',
                'LOGOUT' : 'http://127.0.0.1:8000/api/logout/'   
            }
            return Response(content)

        else:

            # content for non super user
            content = {
                'PROJECT NAME':'EMPLOYEE MANAGMENT SYSTEM',
                '---------------':'-----------------------------',
                'LOGIN-USER' : str(user),
                'LOGIN-USER-PROFILE' : 'http://127.0.0.1:8000/profile/',
                '::::::::::::::':'::::::::::::::::::',
                'CREATE LEAVE APPLICATION' : 'http://127.0.0.1:8000/accounts/employee/leave-application/create/',
                'LEAVE APPLICATION LIST':'http://127.0.0.1:8000/accounts/employee/leave-applications/',
                'LEAVE APPLICATION DETAILS' : 'http://127.0.0.1:8000/accounts/employee/leave-application/detail/<id>/',
                '.......................':'...................................',
                'LOGOUT' : 'http://127.0.0.1:8000/api/logout/'  
            }
            return Response(content)

# Profile View for the current user
class ProfileView(APIView):

    # Authenticaiton classes
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    # permission classes
    permission_classes = [IsAuthenticated]

    # getting the details of the current user
    def get(self, format=None):

        # Displaying the current user detials 
        content = {
            'user' : str(self.request.user), # current login username
            'auth': str(self.request.auth),  # None
            'email' :str(self.request.user.email), # email of the current user
        }
        return Response(content)