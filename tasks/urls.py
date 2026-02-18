from django.urls import path
from . import views

urlpatterns = [
    path("task", views.main, name='task_url'),
    path("task/add-new", views.add_task),
    path("task/reload", views.reload_task, name='reload_task'),
    path("task/delete/<int:id_delete>", views.delete_task, name='delete_task'),
    path("task/change-status/<int:id_task>", views.change_status,name='change_link'),
]
