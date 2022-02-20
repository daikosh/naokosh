from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class TimelineView(TemplateView):
    template_name = 'timeline.html'