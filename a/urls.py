from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("login",login_user,name="login"),
    path("logout",logout_user,name="logout"),
    path("signup",signup,name="signup"),
    path("register",register,name="register"),
    path("membership_thanks",membership_thanks,name="membership_thanks"),
    path("rent/<str:id>",rent,name="rent"),
    path("successpage",successpage,name="successpage")
]