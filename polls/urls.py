from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='home'),

    # path('choice/<int:pk>/', views.ChoiceDetailView.as_view(), name='choice_detail'),
    # path('choicelist/', views.ChoiceListView.as_view(), name='choice_list'),

    path('home/', views.index),
    path('about/', views.load_about, name='about'),
    path('<int:question_id>/', views.load_vote, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('setLanguage/<str:language>', views.set_language, name='set_language')
]