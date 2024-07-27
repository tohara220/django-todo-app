from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "due_date",
        "is_completed",
        "overdue_status",
    )

    def is_overdue_display(self, obj):
        return obj.is_overdue

    is_overdue_display.short_description = "期限切れ"
    is_overdue_display.boolean = True


admin.site.register(Todo, TodoAdmin)
