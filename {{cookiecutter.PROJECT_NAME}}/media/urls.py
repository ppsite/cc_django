from django.urls import path, include
from rest_framework.routers import DefaultRouter

from media.views import ExternalImageViewSets

router = DefaultRouter()
router.register(r'images', ExternalImageViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
