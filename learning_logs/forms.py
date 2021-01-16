from django import forms


from .models import Topic, Entry#Topicはp223で新規, Entryはp227で追加


class TopicForm(forms.ModelForm):#p223
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):#p228
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
