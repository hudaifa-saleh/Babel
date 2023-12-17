from django.contrib import admin

from powerhouse.moments.models import Moment


@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "user_ids")
    list_filter = ("content", "id")
    search_fields = ("content",)
    date_hierarchy = "timestamp"
    ordering = ("-timestamp",)
    list_display_links = ("id", "user_ids", "timestamp")
