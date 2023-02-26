#Rest
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView

#My imports
from .models import User
from .serializers import UserSerializer,UserRegisterSerializer
from .models import User
from .serializers import UserSerializer,UserRegisterSerializer


# REGISTER
class UsersAPIRegisterSet(GenericViewSet, ListModelMixin, 
                        RetrieveModelMixin, CreateModelMixin, 
                        UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ('create',):
            return UserRegisterSerializer
        return UserSerializer

    
