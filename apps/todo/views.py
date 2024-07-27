from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from apps.todo.models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todos"


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_detail.html"
    context_object_name = "todo"


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description"]
    template_name = "todo_create.html"
    success_url = reverse_lazy("todo_list")
