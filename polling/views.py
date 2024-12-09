from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponseRedirect
from polling.models import Poll


class PollListView(ListView):
    model = Poll
    template_name = "polling/list.html"
    context_object_name = "polls"


class PollDetailView(DetailView):
    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        poll = self.get_object()
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
        return HttpResponseRedirect(self.request.path_info)


def list_view(request):
    context = {"polls": Poll.objects.all()}
    return render(request, "polling/list.html", context)


def detail_view(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {"poll": poll}
    return render(request, "polling/detail.html", context)
