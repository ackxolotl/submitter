from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.utils.html import escape

from .models import Submission
import datetime


# Create your views here.
def index(request):
    submissions = Submission.objects.filter(
        created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30),
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
    except ValidationError:
        return HttpResponse('{} is not a valid URL.'.format(escape(url)))

    submission.save()

    return HttpResponse('OK', status=200)


def upvote(request, submission_id):
    submission = Submission.objects.filter(id=submission_id).first()

    if submission:
        submission.upvotes += 1
        submission.save()

        return redirect(index)
    else:
        return HttpResponse('Nothing to upvote.', status=404)
