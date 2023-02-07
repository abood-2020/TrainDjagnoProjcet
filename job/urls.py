from django.urls import path , include
from .views import job_list
urlpatterns = [
    path('' ,job_list )
]
