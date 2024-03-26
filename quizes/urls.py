from django.urls import path
from .views import home_page, start_quiz, quiz_view, quiz_data_view, save_quiz_view

urlpatterns = [
    path('', home_page, name='home'),
    path('data/', start_quiz, name='start-quiz'),
    path('<str:slug>/', quiz_view, name='quiz-view'),
    path('<str:slug>/data/', quiz_data_view, name='quiz-data'),
    path('<str:slug>/save/', save_quiz_view, name='save-quiz-view')
]
