from django.urls import path
from .views import *

app_name = "user_site"

urlpatterns = [
    path("", login_view, name="login"),
    path("home/", login_view, name="home"),
]
