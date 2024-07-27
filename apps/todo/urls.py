from django.urls import path

from apps.todo.views import TodoCreateView, TodoDetailView, TodoListView, TodoUpdateView

urlpatterns = [
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("todos/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todos/<uuid:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("todos/<uuid:pk>/update/", TodoUpdateView.as_view(), name="todo_update"),
]
