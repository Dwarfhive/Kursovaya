from django.urls import path
from digonal import views

urlpatterns = [
    path("diag", views.main),
]