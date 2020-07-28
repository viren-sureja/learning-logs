from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {"text":''}

#  The code at above tells Django not to generate a label for the text field.

# for new entries
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs = {'cols':80})}

#  A widget is an HTML form element, such as a single-line text box, multi-line text area, or drop-down list


