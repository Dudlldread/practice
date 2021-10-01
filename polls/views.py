#from django.shortcuts import render

from typing import ContextManager
from django.http import HttpResponse, response
from django.template import loader

from polls.models import Question

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list': latest_question_list,
    }
    #output=', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context,request))#output)
# Create your views here.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    response="You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
