from django import forms
from datetime import datetime

class TicketInitialForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'How can we help you?'}))
    description = ""
    date = datetime.now()
    priority = ""
    closed = False
    
class TicketDetailForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    date = datetime.now()
    priority = forms.CharField(label="Priority", max_length=100)
    closed = False