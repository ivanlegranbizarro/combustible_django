from django.urls import path

from .views import MarkList, mark_delete, mark_edit, mark_save

app_name = "combustible"

urlpatterns = [
    path("marks/", MarkList.as_view(), name="mark_list"),
    path("marks/save", mark_save, name="mark_save"),
    path("marks/delete/<int:pk>", mark_delete, name="mark_delete"),
    path("marks/edit/<int:pk>", mark_edit, name="mark_edit"),
]
