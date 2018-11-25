from .serializers import ToDoListSerializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from list_todos.models import List


class ToDoList(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = List.objects.all()
    serializer_class = ToDoListSerializers
    permission_classes = (IsAdminUser,)
