from django.urls import path
from authy.views import (UserProfile, signup, PasswordChange, 
   PasswordChangeDone, EditProfile, addToList, showList, peopleList, peoplelistdelete)

from django.contrib.auth import views as authViews 



urlpatterns = [


   	
      path('profile/edit/', EditProfile, name='edit-profile'),
   	path('signup/', signup, name='signup'),
  

   	path('changepassword/', PasswordChange, name='change_password'),
   	path('changepassword/done/', PasswordChangeDone, name='change_password_done'),


   	path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
   	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
   	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
      path('login/', authViews.LoginView.as_view(template_name='authy/login.html'), name='login'),
      path('logout/', authViews.LogoutView.as_view(), name='logout'),


      path('profile/addstolist', addToList, name='add-to-list'),
      path('mylists', showList, name='show-my-list'),
      path('mylists/<list_id>', peopleList, name='people-list'),
      path('mylists/<list_id>/delete', peoplelistdelete, name='list-people-delete')

      

]