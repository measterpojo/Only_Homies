from django.urls import path
from notification.views import showNotification, deleteNotification


urlpatterns = [
	path('', showNotification, name='show-notifications'),
	path('<noti_id>/delete', deleteNotification, name='delete-notification'),

]