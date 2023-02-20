from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from App import views

urlpatterns = [
    path('', views.IndexView.as_view()), # Url path for the Index Page
    path('profile/', views.ProfileView.as_view()),  # url  path for the profile
]

urlpatterns = format_suffix_patterns(urlpatterns)