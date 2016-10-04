from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Kontrolka, Ktr_Question, Ktr_Choice

def index(request):
    test_list = Kontrolka.objects.order_by('-pub_date')[:5]
    context = {'test_list': test_list}
    return render(request, 'kontrolka/index.html', context)

class QuestionWithAnswers:
    def __init__(self, question):
        self.Question = question
        self.Answers = Ktr_Choice.objects.filter(ktr_question = question)

def detail(request, pk):
    result = []
    for q in Ktr_Question.objects.filter(kontrolka = pk):
        result.append(QuestionWithAnswers(q))
    #result = map(QuestionWithAnswers, Ktr_Question.objects.filter(kontrolka = pk))
	return render(request, 'kontrolka/detail.html', {'questions' : result})

def choice(request, question_id):
    question = get_object_or_404(Ktr_Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
