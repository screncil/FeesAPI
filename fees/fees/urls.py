
from django.urls import path

from allfees.views import AllFeesView


urlpatterns = [
    path("fees/all", AllFeesView.as_view(), name="all-fees")
]
