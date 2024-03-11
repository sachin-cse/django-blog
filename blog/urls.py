from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('save/user/<str:request_type>', views.SaveUser, name="save-user"),
]