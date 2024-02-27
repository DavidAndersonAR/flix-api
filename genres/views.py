from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer

# Create your views here.

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreReatriveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
