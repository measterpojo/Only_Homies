from django.shortcuts import render, redirect

from .models import Notification


def showNotification(request):
	user = request.user
	notifications =  Notification.objects.filter(user=user).order_by('-date')
	Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

	context = {
		'notifications':notifications
	}

	return render(request, 'notification/notifications.html', context)


def deleteNotification(request, noti_id):
	user = request.user
	Notification.objects.filter(id=noti_id,user=user).delete()
	return redirect('show-notifications')

def countNotifications(request):
	count_notifications = None
	if request.user.is_authenticated:
		count_notifications = Notification.objects.filter(user = request.user , is_seen=False).count()
	return {'count_notifications': count_notifications}