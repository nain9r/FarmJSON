from django.urls import path
from . import views

urlpatterns = [
    path('json_data', views.get_json_data, name='json_data'),
]