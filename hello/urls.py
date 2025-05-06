from django.urls import path
from hello import views

urlpatterns = [
    path("hello_app/", views.home, name="hello_app"),
]
