from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from account.views import CurrentViewSet

router = DefaultRouter()
router.register(r'current', CurrentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),
]
