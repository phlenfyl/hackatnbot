from django.urls import path


from . views import *


app_name = 'userauth'


urlpatterns =[
    path('signup/', SingUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]