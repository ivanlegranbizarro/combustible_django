from django.urls import include, path

from .views import SignUp

app_name = "users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", SignUp.as_view(), name="signup"),
]
