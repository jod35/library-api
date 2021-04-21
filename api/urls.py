from django.urls import path
from . import views


urlpatterns = [path("", views.BookApiView.as_view(), name="home")]
