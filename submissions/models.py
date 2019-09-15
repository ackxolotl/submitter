from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Submission(models.Model):
    """
    A submission to the klopapier
    """

    url = models.URLField(
        _('URL'),
    )

    upvotes = models.IntegerField(
        _('upvotes'),
        default=0,
    )

    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
    )
