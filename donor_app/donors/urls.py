from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False), name='index'),  # Redirect to login
    path('dashboard/', views.donor_dashboard, name='donor_dashboard'),
]