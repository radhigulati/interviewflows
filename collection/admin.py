from django.contrib import admin

# import your model
from collection.models import Questions

# set up automated slug creation
class QuestionsAdmin(admin.ModelAdmin):
    model = Questions
    # list_display tell Django that we want the name and desc of our fields to
    # show up in admin
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Questions, QuestionsAdmin)

