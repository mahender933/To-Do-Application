from rest_framework import serializers
from list_todos.models import List


class ToDoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('pk', 'item', 'completed', 'added_at', 'updated_at')
        read_only_fields = ['pk']
