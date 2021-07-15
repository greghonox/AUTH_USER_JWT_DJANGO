from django.urls import include, path

from todo.views import HelloApiView

urlpatterns = [
    path("hello/", HelloApiView.as_view()),
]
