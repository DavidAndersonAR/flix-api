from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorSerializers

class ActorCreatelistView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class= ActorSerializers

class ActorRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class= ActorSerializers