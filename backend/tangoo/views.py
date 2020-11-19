from rest_framework import generics
from .models import Tangoo
from .serializers import TangooSerializer


class ListTangoo(generics.ListAPIView):
    queryset = Tangoo.objects.all()
    serializer_class = TangooSerializer


class DetailTangoo(generics.RetrieveAPIView):
    queryset = Tangoo.objects.all()
    serializer_class = TangooSerializer