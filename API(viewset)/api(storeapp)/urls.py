from django.urls import path 
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('products',ProductViewSet)
router.register('category',CategoryViewSet)

urlpatterns = router.urls