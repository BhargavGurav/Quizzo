from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quizPage', views.quizPage, name='quizPage'),
    path('check/', views.answerCheck, name='checker'),
]
