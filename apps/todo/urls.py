from django.urls import path
from django.views.generic import RedirectView

from apps.todo.views import (
    TodoCreateView,
    TodoDeleteView,
    TodoDetailView,
    TodoListView,
    TodoUpdateView,
)

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="todo_list", permanent=True)),
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("todos/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todos/<uuid:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("todos/<uuid:pk>/update/", TodoUpdateView.as_view(), name="todo_update"),
    path("todos/<uuid:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
]
