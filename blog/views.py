from django.views.generic import ListView, DetailView

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
        context["comments"] = Comment.objects.filter(blog=self.object)
        return context
