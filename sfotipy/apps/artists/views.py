from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Artist

class ArtistDetailView(DetailView):

    model = Artist
    context_object_name = 'ArtistDetail'
    template_name = 'artists.html'

class ArtistiListView(ListView):

    model = Artist
    context_object_name = 'Artists'
    template_name = 'artists.html'



from rest_framework import viewsets, serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    # paginate_by = 3
    class Meta:
        model = Artist
        # fields = ('first_name', 'last_name', )

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # paginate_by = 3
    # page_size = 3


# router = routers.DefaultRouter()
# router.register(r'artists', UserViewSet)

# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
#
# # Serializers define the API representation.
#
# # ViewSets define the view behavior.
#
# # Routers provide an easy way of automatically determining the URL conf.
