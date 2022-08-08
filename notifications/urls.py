from django.urls import path
from .views import show_notifications, delete_notification

urlpatterns = [
    path('', show_notifications, name='show_notifications'),
    path('<notification_id>/usun', delete_notification, name='delete_notification'),
]
