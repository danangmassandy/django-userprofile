from django.urls import path

from .views import ListProfilesView

urlpatterns = [
    path('profiles/', ListProfilesView.as_view(), name='profiles-all'),
]