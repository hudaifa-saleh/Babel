from django.urls import path

from babel.moments.views import MomentsListView

urlpatterns = [
    path("list", MomentsListView.as_view(), name="moments-list"),
]
