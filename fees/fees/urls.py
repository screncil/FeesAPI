
from django.urls import path
from allfees.views import AllFeesView, TransportFeesView, EquipmentFeesView, DronesFeesView


urlpatterns = [
    path("fees/all", AllFeesView.as_view(), name="all-fees"),
    path("fees/transport", TransportFeesView.as_view(), name="transport-fees"),
    path("fees/equipment", EquipmentFeesView.as_view(), name="equipment-fees"),
    path("fees/drones", DronesFeesView.as_view(), name="drones-fees")
]
