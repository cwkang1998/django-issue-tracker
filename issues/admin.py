from django.contrib import admin
from issues.models import Issue
from import_export.admin import ImportExportModelAdmin


class IssueAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "status",
        "project",
        "reported_by",
        "assigned_to",
    )
    filter_horizontal = ("linked_issues",)


admin.site.register(Issue, IssueAdmin)
