from django.db import models
from django.utils.translation import gettext_lazy as _

from uuid import uuid4


class Submission(models.Model):
    """
    A submission to the klopapier
    """

    url = models.URLField(
        _('URL'),
        unique=True,
    )

    secret = models.UUIDField(
        _('secret'),
        default=uuid4,
        unique=True,
    )

    upvotes = models.PositiveIntegerField(
        _('upvotes'),
        default=1,
    )

    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
    )

    def __str__(self):
        return self.url
