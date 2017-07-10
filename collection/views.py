from django.shortcuts import render
from collection.models import Questions

def index(request):
    # urls.py will catch that someone wants the homepage and points to this
    # piece of code which will render the index.html template
    # render combines a given template with a given context dictionary and
    # returns a HTTPResponse object with that rendered text
    # render(request, template_name)
    # When the index page is viewed, find all the questions in our DB, display
    # this template, and pass those things along to the template
    #questions = Questions.objects.filter(name__contains='Unique String')
    questions = Questions.objects.all()
    return render(request, 'index.html', {
        'questions': questions,
    })

def questions_detail(request, slug):
    # grab the object
    question = Questions.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'questions/question_detail.html', {
    })
