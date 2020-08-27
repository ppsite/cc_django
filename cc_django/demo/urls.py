from rest_framework.routers import DefaultRouter
from django.urls import path, include
from demo.views import DemoViewSets

router = DefaultRouter()
router.register(r'demo', DemoViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
