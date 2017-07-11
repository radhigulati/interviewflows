from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views

urlpatterns = [
    # url() encases the entry to indicate it's url entry
    # r'^$' is the beginning of the URL pattern
    # views.index means that we'll use the index view in views
    # name='home' is optional but allows us to assign a name to this url so we
    # can refer to it in the future as 'home'
    # Another way to layout the url is:
    # url(
        # regex=r'^$',
        # view=views.index,
        # name='home'
    # )
    url(r'^$', views.index, name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    #r'^questions/: "starts with questions"
    #(?P<slug>[-\w]+)/$: "matches any word and call it 'slug' and 'slug' can be
    # changed for other uses 
    # 'collection.views.question_detail': We are using the soon to be created
    # thing_detail view
    # , name='question_detail': This URL is named question_detail
    url(r'^questions/(?P<slug>[-\w]+)/$', views.question_detail,
        name='questions_detail'),
    url(r'^admin/', admin.site.urls),
]
