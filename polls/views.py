#from django.shortcuts import render

from datetime import timezone
from typing import ContextManager
from django import template
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name= 'latest_question_list'  

    def get_queryset(self):
        #return the last 5 question if you want can change the number of question to charge
        return Question.objects.order_by('-pub_date')[:5]
    


class DetailView(generic.DetailView):
    model= Question
    template_name='polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

"""def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list': latest_question_list,
    }
    output=', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context,request))#output)
 latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

# Create your views here."

def detail(request, question_id):"
    question= get_object_or_404(Question,pk=question_id)"""
    #try:
    #    question= Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #   raise Http404("Question does not exist")
    #return render(request,'polls/detail.html',{'question': question})"""
    #return HttpResponse("You're looking at question %s." % question_id)

"""
def results(request,question_id):
    question= get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html', {'question':question})
      """
    #response="You're looking at the results of questions %s."
    #return HttpResponse(response % question_id)
  

def vote(request, question_id):
    question= get_object_or_404(Question, pk= question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html', {
            'question':question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))#HttpResponse("You're voting on question %s." % question_id)
   

def get_queryset(self):
    """return the last five published questions (not including those set
    tobe published in the future)."""
    return Question.objects.filter(pub_date_lte=timezone.now()).order_by('-pub_date')[:5]
