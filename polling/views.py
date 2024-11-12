# Views for the polling app

from django.shortcuts import render, get_object_or_404
from .models import Poll

def list_view(request):
    polls = Poll.objects.all()
    return render(request, 'polling/list.html', {'polls': polls})

def detail_view(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == "POST":
        poll.score += 1 if request.POST.get("vote") == "Yes" else -1
        poll.save()
    return render(request, 'polling/detail.html', {'poll': poll})

