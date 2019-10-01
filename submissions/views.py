from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from .models import Submission
import datetime


def index(request):
    submissions = Submission.objects.filter(
        created_at__gt=datetime.datetime.today()-datetime.timedelta(days=90),
    ).order_by('-upvotes', '-created_at').all()

    context = {
        'submissions': submissions,
    }

    return render(request, 'submissions/index.html', context)


def create(request):
    url = request.GET.get('url', '')

    submission = Submission(url=url)

    try:
        submission.full_clean()
    except ValidationError as e:
        return HttpResponse('. '.join(e.messages))

    submission.save()

    context = {
        'submission': submission,
    }

    return render(request, 'submissions/create.html', context)


def delete(request, secret):
    submission = Submission.objects.filter(secret=secret).first()
    if submission and submission.delete():
        return HttpResponse('Submission deleted.')
    else:
        return HttpResponse('Nothing to delete.', status=404)


def upvote(request, submission_id):
    submission = Submission.objects.filter(id=submission_id).first()

    if submission:
        submission.upvotes += 1
        submission.save()

        return redirect(index)
    else:
        return HttpResponse('Nothing to upvote.', status=404)
