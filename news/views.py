from django.shortcuts import render, redirect, get_list_or_404
from django.views import generic
from django.conf import settings
from newsapi import NewsApiClient
import requests
import json
from.models import Topics


class IndexView(generic.TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['topic'] = get_list_or_404(Topics, domain_tags=self.kwargs.get("country_name"))
        context['domain'] = self.kwargs.get("country_name")
        context['news_type'] = 'all'
        return context


class TopIndexView(generic.TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super(TopIndexView, self).get_context_data(**kwargs)
        context['topic'] = get_list_or_404(Topics, domain_tags=self.kwargs.get("country_name"), top_news="top")
        context['domain'] = self.kwargs.get("country_name")
        context['news_type'] = 'top'
        return context


class ForeignView(generic.TemplateView):
    template_name = "news/foreign.html"
    def get_context_data(self, **kwargs):
        context = super(ForeignView, self).get_context_data(**kwargs)
        api_world = " https://coronavirus-19-api.herokuapp.com/all"
        api = "https://coronavirus-19-api.herokuapp.com/countries"
        api_japan = "https://coronavirus-19-api.herokuapp.com/countries/japan"
        r_world = requests.get(api_world)
        r = requests.get(api)
        r_japan = requests.get(api_japan)
        data_world = json.loads(r_world.text)
        data = json.loads(r.text)
        data_jp = json.loads(r_japan.text)
        context['corona'] = sorted(data, key=lambda x:x['cases'], reverse=True)
        context['world_corona'] = data_world
        context['jp_corona'] = data_jp

        return context


# Create your views here.
