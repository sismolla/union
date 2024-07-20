from django.urls import reverse_lazy
from .views import homepage,dashboard,profile,logout
from django.urls import path,reverse_lazy


app_name = 'home'

urlpatterns = [
    path('home/',homepage,name='home' ),
    path('hdashboard/',dashboard,name='hdashboard' ),
    # path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),

    ]