# coding: utf-8
"""
Nyuseu - 뉴스 - Views Board
"""
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from nyuseu.models import MyBoard, MyBoardFeeds
from nyuseu.forms import MyBoardFeedsFormset, MyBoardForms
from nyuseu.views import FoldersMixin


class MyBoardFormsSetValid:
    """
        mixin for formset validation
    """
    form_class = MyBoardForms
    model = MyBoard

    def get_context_data(self, **kw):
        context = super(MyBoardFormsSetValid, self).get_context_data(**kw)
        if self.request.POST:
            context['myboardfeeds_form'] = MyBoardFeedsFormset(self.request.POST)
        else:
            context['myboardfeeds_form'] = MyBoardFeedsFormset(instance=self.object)

        if 'slug' in self.kwargs:
            context['name'] = self.kwargs['slug']

        return context

    def form_valid(self, form):

        formset = MyBoardFeedsFormset((self.request.POST or None), instance=self.object)

        if formset.is_valid():

            name = form.cleaned_data.get("name")
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            messages.add_message(self.request, messages.INFO, f'Multiboard {name} saved')

            return HttpResponseRedirect(reverse('board', args=[name]))
        else:

            variables = {'form': form,
                         'formset': formset,
                         "err": formset.errors}

            if 'slug' in self.kwargs:
                variables["name"] = self.kwargs['slug']

            return render(self.request, 'nyuseu/myboard_form.html', variables)


class MyBoardCreateView(MyBoardFormsSetValid, CreateView):
    """
        to Create Board
    """
    pass


class MyBoardUpdateView(MyBoardFormsSetValid, UpdateView):
    """
        to Edit Board
    """
    slug_field = 'name'

    def get_success_url(self):
        return reverse('board', args=[self.kwargs['slug']])


class MyBoardListView(FoldersMixin, ListView):
    """
        Articles List of the user Multiboard
    """
    queryset = MyBoardFeeds.objects.none()
    template_name = 'nyuseu/myboards_articles_list.html'

    def get_queryset(self, *args, **kwargs):
        return get_list_or_404(MyBoardFeeds.objects.filter(board__name=self.kwargs['name']))

    def get_context_data(self, **kw):
        context = super(MyBoardListView, self).get_context_data(**kw)
        context['name'] = self.kwargs['name']
        return context
