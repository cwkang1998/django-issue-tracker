from django.contrib import admin
from issues.models import Issue


class IssueAdmin(admin.ModelAdmin):
    fields = ("name", "description", "status", "project", "reported_by", "assigned_to")


admin.site.register(Issue, IssueAdmin)
