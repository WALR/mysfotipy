from django.contrib import admin

from .models import Track
from .actions import export_as_excel

class TrackAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'order', 'album', 'player')
    list_filter = ('artist', 'album')
    search_fields = ('title', 'artist__first_name', 'artist__last_name')
    list_editable = ('title',)
    actions = (export_as_excel, )
    raw_id_fields = ('artist', )

admin.site.register(Track, TrackAdmin)
