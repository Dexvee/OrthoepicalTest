from django.urls import path
from .views import index_view, dict_view


urlpatterns = [
    path('', index_view),
    path('dict/', dict_view),
]
