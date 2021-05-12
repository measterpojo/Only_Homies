
from django.contrib import admin
from django.urls import path, include

from authy.views import UserProfile, removeFromList

from tier.views import subscribe

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', include('authy.urls')),
    path('sub/', include('tier.urls')),
    path('post/', include('posts.urls')),
    path('notifications/', include('notification.urls')),
    path('messages/', include('direct.urls')),
 
    path('<username>/', UserProfile, name='profile'),
    path('<username>/photos', UserProfile, name='profilephotos'),
    path('<username>/videos', UserProfile, name='profilevideos'),

    path('<username>/<tier_id>/subscribe/', subscribe, name='subscribe'),
    path('<username>/remove/fromlist', removeFromList, name='remove-from-list')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
