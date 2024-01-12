from django.views.generic import ListView, DetailView

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
