from django.views.generic import ListView, DetailView

from property.models import Property
from .models import Agent


class AgentListView(ListView):
    template_name = "agent/index.html"
    model = Agent
    context_object_name = 'agents'
    paginate_by = 6


class AgentDetailView(DetailView):
    template_name = "agent/agent-detail.html"
    model = Agent
    context_object_name = 'agent'

    def get_context_data(self, **kwargs):
        context = super(AgentDetailView, self).get_context_data(**kwargs)
        # TODO: Sorting will be added to properties on page
        context["properties"] = Property.objects.filter(agent=self.object)[:6]
        return context
