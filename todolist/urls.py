from django.urls import path

from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name="index"),
    path('edit_task/<int:pk>',
    views.update_task, name="task"),
    path('delete_task/<int:pk>',
    views.delete_task, name="del_task"),
]