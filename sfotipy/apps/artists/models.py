from django.db import models


class Artist(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(blank=True, max_length=255)
    biography = models.TextField(blank=True)
    
