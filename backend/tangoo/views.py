from rest_framework import generics
from .models import Tangoo
from .serializers import TangooSerializer
# from rest_framework.permissions import IsAuthenticated


class ListTangoo(generics.ListCreateAPIView):
    queryset = Tangoo.objects.all()
    serializer_class = TangooSerializer
    # permission_classes = (IsAuthenticated,)


class DetailTangoo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tangoo.objects.all()
    serializer_class = TangooSerializer
