from rest_framework import generics
from ..models import Kid
from .serializers import KidSerializer



class KidListView(generics.ListAPIView):
	queryset = Kid.objects.all()
	serializer_class = KidSerializer

class KidDetailView(generics.RetrieveAPIView):
	queryset = Kid.objects.all()
	serializer_class = KidSerializer

class KidCreateView(generics.CreateAPIView):
	queryset = Kid.objects.all()
	serializer_class = KidSerializer