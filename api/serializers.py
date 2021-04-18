from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from api.models import Note


class NoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'user', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']