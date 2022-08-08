from django.shortcuts import render, redirect
from notifications.models import Notification
# Create your views here.
def show_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by("-date")
    notifications.update(is_seen=True)
    context = {'notifications': notifications}
    return render(request, 'notifications.html', context)


def delete_notification(request, notification_id):
    user = request.user
    Notification.objects.filter(id=notification_id, user=user).delete()
    return redirect('show_notifications')


def count_notifications(request):
    notifications_count = 0
    if request.user.is_authenticated:
        notifications_count = Notification.objects.filter(user=request.user, is_seen=False).count()

    return {'notifications_count': notifications_count}