from django.conf import settings
from django.db import models


class StatusChoice(models.IntegerChoices):
    OPEN = 0
    IN_PROGRESS = 1
    WONT_FIX = 2
    RESOLVED = 3


class Issue(models.Model):
    """
    Represents each issues reported by someone.

    Setting foreign relations to protect, since we should allow for deletion
    of any users without activities, but if they already have activity, they shouldn't be
    able to be deleted easily
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(
        default=StatusChoice.OPEN, choices=StatusChoice.choices
    )
    linked_issues = models.ManyToManyField(to="Issue", blank=True)
    project = models.ForeignKey(to="project.Project", on_delete=models.PROTECT)
    reported_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="%(class)s_reported",
    )
    assigned_to = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="%(class)s_assigned",
    )

    def __str__(self) -> str:
        return self.name
