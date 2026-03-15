from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *


urlpatterns = [

    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),

    path('logout/', LogoutView.as_view(), name="logout"),

    path('signup/', signup, name="signup"),

    path('profile/', profile, name="profile"),

    path('profile/edit/', edit_profile, name="edit_profile"),

]