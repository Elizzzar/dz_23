from django.urls import path
from .views import home_auth,user_auth, Sign_Up, Log_out, Login
urlpatterns = [
    path('', user_auth, name= 'user_auth'),
    path('home/', home_auth, name = 'home'),
    path('sign_up/', Sign_Up.as_view(), name='sign_up'),
    path('login/', Login.as_view(), name='login'),
    path('log_out/', Log_out.as_view(), name='log_out'),
]