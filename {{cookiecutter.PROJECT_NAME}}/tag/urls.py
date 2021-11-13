from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tag.views import ColoredTagViewSets

router = DefaultRouter()
router.register(r'tag', ColoredTagViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
