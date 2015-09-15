from .models import Track

from rest_framework import serializers



class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        # fields = ('first_name', 'last_name', )
