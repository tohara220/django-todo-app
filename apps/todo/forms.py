from django import forms

from apps.todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "due_date", "is_completed"]
