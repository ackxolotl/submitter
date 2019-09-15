from django.db import models
from django.utils.translation import gettext_lazy as _

from uuid import uuid4


# Create your models here.
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

    upvotes = models.IntegerField(
        _('upvotes'),
        default=0,
    )

    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
    )
