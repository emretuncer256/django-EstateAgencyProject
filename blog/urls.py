from django.urls import path

from .views import BlogListView, BlogDetailView

app_name = "blog"
urlpatterns = [
    path('', BlogListView.as_view(), name="index"),
    path('<slug:slug>/', BlogDetailView.as_view(), name="detail"),
]
