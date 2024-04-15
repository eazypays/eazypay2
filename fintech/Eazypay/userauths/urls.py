from django.urls import path,include
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("signup/", views.RegisterView, name="signup"),
    path("login/", views.LoginView, name="login" ),
    path("login/signup", views.RegisterView, name="signup" ),
      path("signup/login", views.LoginView, name="signup" ),
    
    # path("sign-in/", views.LoginView, name="sign-in"),
    # path("sign-out/", views.logoutView, name="sign-out"),
    #  path("", views.index, name = 'index.html')
   
]
