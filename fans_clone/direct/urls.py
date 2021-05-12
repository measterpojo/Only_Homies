from .views import (peopleWeCanMessage, newConversation, 
	inbox, directs, usersearch, sendDirect, loadMore)

from django.urls import path


urlpatterns = [

	path('', inbox, name='inbox'),
	path('start/', peopleWeCanMessage, name='people-we-can-message'),
	path('new/<username>', newConversation, name='new-conversation'),
	path('directs/<username>', directs, name='directs'),
	path('search/', usersearch, name='user-search'),
	path('send/', sendDirect, name='send-direct'),
	path('loadmore/', loadMore, name='loadmore'),


]