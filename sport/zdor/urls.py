from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sport.views import SportItemViewSet, SeasonsViewSet
from story.views import StoryViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('sports', SportItemViewSet)
router.register('seasons', SeasonsViewSet)
router.register('stories', StoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
