from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.logi_n, name="login"),
    path("logout/", views.logou_t, name="logout"),
    path("register/", views.rigiste_r, name="rigister"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("history-logs/", views.history, name="history"),
    path("profile/", views.profile, name="profile"),
    path("settings/", views.settings, name="settings"),
]
