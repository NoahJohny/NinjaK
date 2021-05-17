"""musiqualizerApp URL Configuration"""

from django.urls import path
# Importing views from musiqualizerApp.
from . import views

# App Name (for future reference)
app_name = 'musiqualizerApp'

urlpatterns = [
    # Path to the Homepage View
    path('',views.homepage, name="homepage")
]
