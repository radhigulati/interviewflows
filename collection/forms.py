from django.forms import ModelForm
from collection.models import Questions


class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ('name', 'description',)
