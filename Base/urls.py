from django.urls import path
from .views import AllScenesChoicesView

urlpatterns = [
    path('scenes/', AllScenesChoicesView.as_view(), name='all_scenes_choices'),  # New URL for the combined choices view
]