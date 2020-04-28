from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('writter_profile/<str:pk>',views.writter_profile,name='writter_profile'),
    path('server_info',views.server_info,name='server_info'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('new_poem',views.new_poem,name='new_poem')
]