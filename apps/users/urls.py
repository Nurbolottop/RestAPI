#Django
from django.urls import path

#Rest
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter

#My imports
from .views import UsersAPIRegisterSet

router = DefaultRouter()
router.register(prefix='users', viewset=UsersAPIRegisterSet)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name="api_login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="api_refresh")
]
urlpatterns += router.urls