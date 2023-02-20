from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView, TokenBlacklistView)

urlpatterns = [
    path('', include('App.urls')),
    path('admin/', admin.site.urls),

    path('api/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('accounts/manager/', include('App_Admin.urls')),
    path('accounts/employee/', include('App_Employee.urls')),
]