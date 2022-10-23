from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.template import loader
from django.urls import reverse

from .forms import EmailPostForm
from .models import Question, Choice, Citizen


# utiltty functions


def get_language(the_request):
    try:
        language = the_request.session['language']
    except KeyError:
        language = 'english'

    return language


def set_language(request, language):
    if language in ('english', 'amharic', 'afaan oromo'):
        request.session['language'] = language
    else:
        return HttpResponse(
            'Please enter a valid language. the available languages are: english, afaan oromo and amharic')
    return HttpResponseRedirect(reverse('polls:home'))


def index(request):
    language = get_language(request)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    paginator = Paginator(latest_question_list,
                          3)  # 3 questions per a page (we feed all of the objects for the paginator object)
    page = request.GET.get('page')
    try:
        questions_for_page = paginator.page(page)
    except PageNotAnInteger:
        questions_for_page = paginator.page(1)
    except EmptyPage:
        questions_for_page = paginator.page(paginator.num_pages)
    # note that the render shortcut loads a template, fills it a context and
    # returns an HttpResponse object with the filled template as its body in one go.
    template = loader.get_template('polls/home.html')
    context = {
        'questions': questions_for_page,
        'language': language
    }
    return HttpResponse(template.render(context, request))


def load_vote(request, question_id):
    language = get_language(request)
    # note that the following is a try, load, except 404 code abstracted
    #  under the get_object_or_404 shortcut
    question = get_object_or_404(Question, id=question_id)
    citizen_form = EmailPostForm()
    return render(request, 'polls/vote_page.html', {'question': question,
                                                    'citizen_form': citizen_form,
                                                    'language': language})


def results(request, question_id):
    language = get_language(request)
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question': question, 'language': language})


def vote(request, question_id):
    language = get_language(request)
    question = get_object_or_404(Question, id=question_id)
    citizen_form = EmailPostForm()
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
        voter = Citizen.objects.get(voter_id=request.POST['voter_id'])

        if not (voter.first_name == request.POST['first_name'] and voter.last_name == request.POST['last_name']):
            return render(request, 'polls/vote_page.html',
                          {
                              'question': question,
                              'citizen_form': citizen_form,
                              'voter_error': {'english': "No such a registered user", 'amharic': 'ይቅርታ፤ ያስገቡት የመራጭነት መረጃ አልተመዘገበም', 'afaan_oromo' : 'OROMIC-No such a registered user'},
                              'language': language
                          })

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/vote_page.html',
                      {
                          'question': question,
                          'citizen_form': citizen_form,
                          'choice_error': {'english': "You didn't select a choice", 'amharic': 'ምርጫዎትን አላስገቡም', 'afaan_oromo': "Homaa hin filatne"},
                          'language': language
                      })
    except:
        return render(request, 'polls/vote_page.html',
                      {
                          'question': question,
                          'citizen_form': citizen_form,
                          'voter_error': {'english': "No such a registered user", 'amharic': 'ይቅርታ፤ ያስገቡት የመራጭነት መረጃ አልተመዘገበም', 'afaan_oromo' : "fayyadamaan maqaa kanaan galmaa'e hin jiru"},
                          'language': language
                      })
    else:
        if question not in voter.voted_questions.all():
            # instead of  'selected_choice.votes += 1' , we are using the
            # the F class which prepares an update query and executes it
            #  on the database upon call to 'save()'. this avoids RACE CONDITIONS.
            #  refer to the docs for more info
            selected_choice.votes = F('votes') + 1
            selected_choice.save()
            # add the question to the voted_questions of the voter so that he/she can vote only once
            voter.voted_questions.add(question)
            # Always return an HttpResponseRedirect after successfully
            # dealing with post data. This prevents data from being posted
            # twice if a user hits a back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

        else:
            # the user has previously voted on the question
            error_message = 'You have previously voted on this question. You can only vote once.'
            return render(request, 'polls/vote_page.html',
                          {
                              'question': question,
                              'citizen_form': citizen_form,
                              'choice_error': {'english': 'You have previously voted on this question. You can only vote once.', 'amharic': 'ከዚህ በፊት በዚህ ጠያቄ ላይ መርጠዋል፡፡ በአንድ ጥያቄ ላይ መምረጥ የሚቻለው አንድ ጊዜ ብቻ ነው፡፡', 'afaan_oromo': "Yaada kana irratti dursitee filattee jirta. Al tokkoo ol filachuun hin danda'amu"},
                              'language': language
                          })





'''
THE FOLLOWING VIEW WAS WRITTEN FOR DEMONESTRATION PURPOSES AND IT IS NON-FUNCTIONAL NOW
///////////////////////////////////////////////////////////////////////////////////////
def no_auth_vote(request, question_id):
    language = get_language(request)
    question = get_object_or_404(Question, id=question_id)
    citizen_form = EmailPostForm()
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/vote_page.html',
                      {
                          'question': question,
                          'citizen_form': citizen_form,
                          'choice_error': {'english': "You didn't select a choice", 'amharic': 'ምርጫዎትን አላስገቡም', 'afaan_oromo': "Homaa hin filatne"},
                          'language': language
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
'''


def load_about(request):
    language = get_language(request)
    return render(request, 'polls/about.html', {'language': language})
