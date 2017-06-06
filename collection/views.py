from django.shortcuts import render

def index(request):
    # urls.py will catch that someone wants the homepage and points to this
    # piece of code which will render the index.html template
    # render combines a given template with a given context dictionary and
    # returns a HTTPResponse object with that rendered text
    # render(request, template_name)
    number = 6
    return render(request, 'index.html', {
        'number': number,
    })
