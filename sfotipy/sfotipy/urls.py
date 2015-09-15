from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from apps.artists.views import ArtistiListView

from apps.artists.views import ArtistViewSet
from apps.albums.views import AlbumViewSet
from apps.tracks.views import TrackViewSet

router = routers.DefaultRouter()
router.register(r'artist', ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'track', TrackViewSet)

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-]+)/', 'apps.tracks.views.track_view', name='track_views'),
    url(r'^artists/', ArtistiListView.as_view(), name='track_views'),
    url(r'^signup/', 'apps.userprofiles.views.signup', name='signup_views'),
    url(r'^signin/', 'apps.userprofiles.views.signin', name='signin_views'),
    url(r'^api/', include(router.urls)),
    # url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root':settings.MEDIA_ROOT,}
		),
	]
