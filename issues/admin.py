from django.contrib import admin
from issues.models import Issue
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource


class IssueResource(ModelResource):
    class Meta:
        model = Issue


class IssueAdmin(ImportExportModelAdmin):
    fields = ("name", "description", "status", "project", "reported_by", "assigned_to")


admin.site.register(Issue, IssueAdmin)
