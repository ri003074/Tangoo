from rest_framework import generics
from .models import Tangoo
from .serializers import TangooSerializer


class ListTangoo(generics.ListCreateAPIView):
    queryset = Tangoo.objects.all()
    serializer_class = TangooSerializer


class DetailTangoo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tangoo.objects.all()
    serializer_class = TangooSerializer
