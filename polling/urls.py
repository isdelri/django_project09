from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='poll_list'),  # Adjust view and name as needed
    path('poll/<int:poll_id>/', views.detail_view, name='poll_detail'),
]
