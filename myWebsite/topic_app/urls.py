from django.urls import path, include
from topic_app import views

app_name = 'topic_app'

urlpatterns = [
    path('discussion/', views.discussion, name='discussion'),

]