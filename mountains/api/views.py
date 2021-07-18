from rest_framework import generics
from mountains.models import Mountain
from mountains.api.serializers import MountainSerializer


class ListView(generics.ListCreateAPIView):
    queryset = Mountain.objects.all().order_by("-id")
    serializer_class = MountainSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
