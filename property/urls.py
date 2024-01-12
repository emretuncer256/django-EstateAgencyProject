from django.urls import path

from . import views

app_name = "property"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.index, name="detail")
]
