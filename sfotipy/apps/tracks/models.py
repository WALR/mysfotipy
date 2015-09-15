from django.db import models

from apps.albums.models import Album
from apps.artists.models import Artist

class Track(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
    album = models.ForeignKey(Album)
    artist = models.ForeignKey(Artist)

    def player(self):
        return """
        <audio controls>
            <source src="%s" type="audio/mpeg">
            Tu navegador no soporta el tag audio
        </audio>
        """ % self.track_file.url
    player.allow_tags = True


    def __unicode__(self):
        return self.title
