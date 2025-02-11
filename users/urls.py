from django.urls import path

from users.views import (EmailVerificationView, UserLoginView, UserProfileView,
                         UserRegistrationView, logout)

app_name = 'users'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('registration/', UserRegistrationView.as_view(), name = 'registration'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name = 'profile'),
    path('logout/', logout, name='logout'),
    path('verifi/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),

]