from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path('save/user/<str:request_type>', views.SaveUser, name="save-user"),
    # dashboard access
    path('admin/dashboard', views.admin_dashboard, name="admin-dashboard"),
]