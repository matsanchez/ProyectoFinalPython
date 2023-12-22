from django.urls import path
from .views import RegisterUser, LogoutView, LoginFormView, ProfileView, HandledPermissionView, ChangePasswordFormView


app_name="account"

urlpatterns = [
    path("login/", LoginFormView.as_view(), name="login"),
    path("authenticated/", HandledPermissionView.as_view(), name="authenticated"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("changepassword/", ChangePasswordFormView.as_view(), name="change_password"),
    path("logout/", LogoutView.as_view(template_name='account/logout.html') ,name='logout')
]
