from django import forms
from .models import Todo, TodoList

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = "__all__"