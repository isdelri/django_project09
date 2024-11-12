from django.contrib import admin
from django.urls import path, include
from . import views  # Import home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polling/', include('polling.urls')),   # Include polling app URLs
    path('blogging/', include('blogging.urls')), # Include blogging app URLs
    path('', views.home, name='home'),           # Root URL
]
