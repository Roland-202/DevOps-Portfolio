from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health),
    path("tasks/", views.task_list),
]
