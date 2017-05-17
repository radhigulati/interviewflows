from django.shortcuts import render

def index(request):
    # urls.py will catch that someone wants the homepage and points to this
    # piece of code which will render the index.html template
    return render(request, 'index.html')
