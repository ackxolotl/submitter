from django.contrib import admin

from .models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'upvotes',
        'created_at',
    )


admin.site.register(Submission, SubmissionAdmin)
