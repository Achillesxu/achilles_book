#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : achilles_book
@Time    : 2017/11/6 22:02
@Author  : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site    :
@File    : views.py
@desc    :
"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice

# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def start_index(request):
    i_context = {
        'page_title': 'jinja2 start template',
    }
    return render(request, 'start_index.html', context=i_context)


class PollIndexView(generic.ListView):
    template_name = 'poll_index.html'
    context_object_name = 'latest_question_list'
    http_method_names = ['get', ]

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = 'poll table page'
        context['table_name'] = 'Poll Table'
        return context


class PollDetailView(generic.DetailView):
    model = Question
    template_name = 'poll_detail.html'
    http_method_names = ['get', ]

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'poll question detail'
        context['choice_all'] = self.get_object(queryset=self.get_queryset()).choice_set.all()
        return context


class PollResultView(generic.DetailView):
    model = Question
    template_name = 'poll_result.html'
    http_method_names = ['get', ]

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'poll question result'
        context['choice_all'] = self.get_object(queryset=self.get_queryset()).choice_set.all()
        return context


class AboutPage(generic.TemplateView):
    template_name = 'about.html'
    http_method_names = ['get', ]


class UserRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'user_registration.html'

    def get_success_url(self):
        return reverse('polls:index')
