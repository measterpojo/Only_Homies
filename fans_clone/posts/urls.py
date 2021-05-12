from django.urls import path
from .views import new_post_view, index_view, post_details, likes, bookmark, bookmarkList


urlpatterns = [
	
	path('', index_view, name='index'),

	path('newpost/', new_post_view, name='post'),
	path('bookmarks/', bookmarkList, name='bookmarks'),


	path('<uuid:post_id>', post_details, name='postdetails'),
	path('<uuid:post_id>/like/', likes, name='postlikes'),
	path('<uuid:post_id>/bookmark',bookmark, name='postbookmark'),

]

