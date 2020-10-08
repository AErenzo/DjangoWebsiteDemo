from django.shortcuts import render

# Create your views here.

def topicForm(request):
    return render(request, 'project_app/submit_topic.html')


def researchTopics(request):
    return render(request, 'project_app/research_topics.html')

