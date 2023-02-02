from django.urls import path , include
from . import views
urlpatterns = [
    path('' , views.main),
    path('about' , views.about),
    path('blog' , views.blog),
    path('index' , views.index),
]