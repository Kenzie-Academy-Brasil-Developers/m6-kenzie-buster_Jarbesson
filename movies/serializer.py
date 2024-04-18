from rest_framework import serializers
from movies.models import Movie, RatinChoice


class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_blank=True, default='')
    rating = serializers.ChoiceField(default=RatinChoice.G, choices=RatinChoice.choices)
    synopsis = serializers.CharField(default='', allow_blank=True)
    added_by = serializers.EmailField(read_only=True, source="user.email")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)