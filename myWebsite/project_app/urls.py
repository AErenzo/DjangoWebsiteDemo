from django.urls import path
from project_app import views

app_name = 'project_app'

urlpatterns = [

    path('topic_form/', views.topicForm, name='topic_form'),
    path('topics/', views.researchTopics, name='topics'),
]