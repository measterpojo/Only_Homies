from django.urls import path
from .views import newTier_view, fans_list, followingList, checkExpiration


urlpatterns = [
	path('newtier/',newTier_view, name='newtier'),
	path('my_fans/', fans_list, name='myfans'),
	path('my_follows/', followingList, name='myfollows'),
	path('checkexp/', checkExpiration, name='check')
]