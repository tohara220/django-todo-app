from django.urls import path

from apps.todo.views import TodoCreateView, TodoDetailView, TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("<uuid:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
]
