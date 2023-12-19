from django.contrib import admin
from django.urls import path, include

from powerhouse.accounts.views import HomePageView

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("", HomePageView.as_view(), name="home"),
    path("admin/", admin.site.urls),
]
