from django.urls import path
from authy.views import  Signup, PasswordChange, PasswordChangeDone, EditProfile, user_search

from django.contrib.auth import views as authViews 



urlpatterns = [
   	
    path('profil/edytuj', EditProfile, name='edit_profile'),
   	path('rejestracja/', Signup, name='signup'),
   	path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
   	path('wyloguj/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
	path('szukaj/', user_search, name='user_search'),
   	path('zmiana_hasla/', PasswordChange, name='change_password'),
   	path('zmiana_hasla/gotowe', PasswordChangeDone, name='change_password_done'),
   	path('reset_hasla/', authViews.PasswordResetView.as_view(), name='password_reset'),
   	path('reset_hasla/gotowe', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
   	path('reset_hasla/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('reset_hasla/zakonczone/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]