from django.urls import path

from . import views

urlpatterns = [
    path("list", views.TodoCreateListView.as_view()),
    path("list/<int:pk>", views.TodoDetailView.as_view()),
    path("update/<int:pk>", views.TodoUpdateView.as_view()),
]
