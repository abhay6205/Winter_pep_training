from django.db import models


class TaskList(models.Model):
    """A named list that groups multiple tasks together."""
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def total_tasks(self):
        return self.todos.count()

    @property
    def completed_tasks(self):
        return self.todos.filter(completed=True).count()

    @property
    def pending_tasks(self):
        return self.total_tasks - self.completed_tasks

    @property
    def progress_percent(self):
        total = self.total_tasks
        if total == 0:
            return 0
        return int((self.completed_tasks / total) * 100)


class Todo(models.Model):
    """A single task that belongs to a TaskList."""
    task_list = models.ForeignKey(
        TaskList, on_delete=models.CASCADE, related_name='todos'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
