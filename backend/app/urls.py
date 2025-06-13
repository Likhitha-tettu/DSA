from django.urls import path,include
from rest_framework import routers
from .views import BooksViewSet

#Django Rest Framework provides routing options for CRUD operations by default 
router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)


urlpatterns = [
    path('', include(router.urls)),
]