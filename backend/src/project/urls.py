from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('snippets.urls')),
    path('calc/', include('calculator.urls')),
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
