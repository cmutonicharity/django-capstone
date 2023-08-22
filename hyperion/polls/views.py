from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Question, Choice


# Create your views here.
@login_required(redirect_field_name="redirect", login_url=reverse_lazy('user_auth:login'))
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)


@login_required(redirect_field_name="redirect", login_url=reverse_lazy('user_auth:login'))
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


@login_required(redirect_field_name="redirect", login_url=reverse_lazy('user_auth:login'))
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {'question': question})


@login_required(redirect_field_name="redirect", login_url=reverse_lazy('user_auth:login'))
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully
        # dealing with POST data. This prevents data from being
        # posted twice if a user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )
