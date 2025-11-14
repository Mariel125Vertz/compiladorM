from django.urls import path # type: ignore
from.import views

urlpatterns = [
    path("code", views.main),
]
