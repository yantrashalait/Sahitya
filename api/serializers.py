from rest_framework import serializers
from core.models import AudioBook

class AudioBookSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = AudioBook
        fields = ('id', 'title', 'author', 'publication', 'audio_file', 'price', 'image')