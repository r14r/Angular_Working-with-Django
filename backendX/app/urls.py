from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Pastebin API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path(r'^', include('snippets.urls')),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'^schema/$', schema_view),
    path(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
