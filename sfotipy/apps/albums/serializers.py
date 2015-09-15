from .models import Album

from rest_framework import serializers



class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        # fields = ('first_name', 'last_name', )
