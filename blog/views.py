from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddCommentForm
from .models import Blog, Comment


class BlogListView(ListView):
    model = Blog
    paginate_by = 6
    template_name = "blog/index.html"
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog-detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(blog=self.object, status=True).order_by('-created_at')
        context["comment_form"] = AddCommentForm(initial={'blog': self.object})
        return context


class AddCommentView(CreateView):
    form_class = AddCommentForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Comment submitted successfully!")
        return response

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'slug': self.kwargs['slug']})
