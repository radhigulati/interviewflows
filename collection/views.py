from django.shortcuts import render, redirect
from collection.forms import QuestionForm
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


def question_detail(request, slug):
    # grab the object
    question = Questions.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'questions/questions_detail.html', {
    })

def edit_question(request, slug):
    # grab the object
    question = Questions.objects.get(slug=slug)
    # set the form we're using...
    form_class = QuestionForm
    # if we're coming tot his view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=question)
        if form.is_valid():
            # save the new data
            form.save()
            return rediirect('questions_detail', slug=question.slug)

        # otherwise just create the form
    else:
        form = form_class(instance=question)

    # and render the template
    return render(request, 'questions/edit_question.html', {
        'question': question,
        'form': form,
    })
