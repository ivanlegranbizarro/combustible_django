from django.urls import path

from .views import primera_vista

app_name = "base"

urlpatterns = [
    path("", primera_vista, name="primera_vista"),
]
