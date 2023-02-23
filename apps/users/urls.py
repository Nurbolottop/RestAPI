#Django
from django.urls import path

#Rest
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

#My imports
from .views import UsersAPIViewSet,UsersAPI

router = DefaultRouter()
router.register(prefix='api/register/', viewset=UsersAPIViewSet)

urlpatterns = [
    path('api/users/', UsersAPI.as_view(), name= "api_user"),
    path('api/login/', TokenObtainPairView.as_view(), name="api_login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="api_refresh")
]
urlpatterns += router.urls