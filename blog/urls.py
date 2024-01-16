from django.urls import path

from .views import BlogListView, BlogDetailView, AddCommentView

app_name = "blog"
urlpatterns = [
    path('', BlogListView.as_view(), name="index"),
    path('<slug:slug>/', BlogDetailView.as_view(), name="detail"),
    path('<slug:slug>/add_comment/', AddCommentView.as_view(), name="add-comment"),
]
