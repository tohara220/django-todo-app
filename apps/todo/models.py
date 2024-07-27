import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.html import format_html


class Todo(models.Model):
    """TODOを管理するモデル"""

    uuid = models.UUIDField(
        verbose_name="ID",
        help_text="ID",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(
        verbose_name="タイトル",
        help_text="タスクのタイトルを入力してください",
        max_length=256,
        blank=False,
        null=False,
        unique=False,
        default="",
    )
    description = models.TextField(
        verbose_name="内容",
        help_text="タスクの詳細を入力してください",
        blank=True,
        null=False,
        unique=False,
        default="",
    )
    due_date = models.DateField(
        verbose_name="期限",
        help_text="デフォルトでは5日後が設定されています",
        default=timezone.now() + timedelta(days=5),
    )
    is_completed = models.BooleanField(
        verbose_name="完了",
        help_text="完了したらTrueにしてください",
        blank=False,
        null=False,
        unique=False,
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name="作成日時",
        help_text="作成日時",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="更新日時",
        help_text="更新日時",
        auto_now=True,
    )

    @property
    def is_overdue(self):
        now = timezone.now().date()
        due_date = self.due_date
        completed = self.is_completed
        return now > due_date and not completed

    @property
    def overdue_status(self):
        now = timezone.now().date()
        if self.is_completed:
            return format_html('<span style="color: green;">✔</span>')
        elif now > self.due_date:
            return format_html('<span style="color: red;">✖</span>')
        else:
            return format_html('<span style="color: orange;">⏳</span>')

    def __str__(self):
        return self.title
