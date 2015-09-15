from django.contrib import admin

from .models import Artist
from apps.tracks.models import Track
from apps.albums.models import Album

class TrackInLine(admin.StackedInline):
    model = Track
    extra = 1

class AlbumInLine(admin.StackedInline):
    model = Album
    extra = 1

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', )
    inlines = [TrackInLine, AlbumInLine, ]

admin.site.register(Artist, ArtistAdmin)
