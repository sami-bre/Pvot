from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from . models import Question, Choice
from django.db.models import F
from django.template import loader
from django.views import generic
from django.http import Http404
from django.urls import reverse

"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # note that the render shortcut loads a template, fills it a context and 
    # returns an HttpResponse object with the filled template as its body in one go. 
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # note that the following is a try, load, except 404 code abstracted
    #  under the get_object_or_404 shortcut
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/vote_page.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question' : question})
"""

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/vote_page.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,'polls/vote_page.html',
                        {
                            'question' : question,
                            'error_message' : "You didn't select a choice"
                        })
    else:
        # instead of  'selected_choice.votes += 1' , we are using the 
        # the F class which prepares an update query and executes it
        #  on the database upon call to 'save()'. this avoids RACE CONDITIONS.
        #  refer to the docs for more info
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully
        # dealing with post data. This prevents data from being posted
        # twice if a user hits a back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class ChoiceDetailView(generic.DetailView):
    model = Choice


class ChoiceListView(generic.ListView):
    def get_queryset(self):
        return Choice.objects.all()