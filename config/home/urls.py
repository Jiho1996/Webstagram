from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('board/',views.board,name='home_board'),
]