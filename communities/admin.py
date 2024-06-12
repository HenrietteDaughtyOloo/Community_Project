from django.contrib import admin
from .models import Community

admin.site.register(Community, list_display=('name', 'description', 'admin', 'created_at'))
