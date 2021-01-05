from rest_framework import generics
from .models import Tangoo
from .serializers import TangooSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ListTangoo(generics.ListCreateAPIView):
    queryset = Tangoo.objects.all()
    serializer_class = TangooSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class DetailTangoo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tangoo.objects.all()
    serializer_class = TangooSerializer
