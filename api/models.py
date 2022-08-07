from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Task(models.Model):

    class PriorityChoices(models.TextChoices):
        ONE = '1', _('Priority 1')
        TWO = '2', _('Priority 2')
        THREE = '3', _('Priority 3')
        FOUR = '4', _('Priority 4')

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    is_done = models.BooleanField(default=False)

    due_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    priority = models.CharField(
        max_length=1,
        choices=PriorityChoices.choices,
        default=PriorityChoices.FOUR
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='child_tasks',
        related_query_name='child_task',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks',
        related_query_name='task'
    )

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
