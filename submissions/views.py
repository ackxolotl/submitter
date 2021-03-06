from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
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
    if submission:
        if submission.delete():
            return HttpResponse('Submission deleted.')
        else:
            return HttpResponse('Submission could not be deleted.', status=500)
    else:
        return HttpResponse('Nothing to delete.', status=404)


def upvote(request, submission_id):
    submission = Submission.objects.filter(pk=submission_id).first()

    if submission:
        submission.upvotes = (submission.upvotes + 1) % (1 << 31)
        submission.save()

        return redirect(index)
    else:
        return HttpResponse('Nothing to upvote.', status=404)


def upvote_stats(request):
    submissions = Submission.objects.filter(
        created_at__gt=datetime.datetime.today()-datetime.timedelta(days=90),
    ).order_by('-upvotes', '-created_at').all()

    stats = dict(map(lambda submission: (submission.pk, submission.upvotes), submissions))

    return JsonResponse(stats)
