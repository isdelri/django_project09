# Register the Poll model with the Django admin.

from django.contrib import admin
from .models import Poll

admin.site.register(Poll)
