from django.contrib import admin

from babel.moments.models import Moment


@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp")
    list_filter = ("content", "id")
    search_fields = ("content",)
    date_hierarchy = "timestamp"
    ordering = ("-timestamp",)
    list_display_links = ("id", "timestamp")
