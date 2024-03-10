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
    priority = forms.ChoiceField(label="Priority", choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")])
    closed = False
    
class CommentForm(forms.Form):
    comment = forms.CharField(label="Leave a comment", max_length=350, widget=forms.Textarea)
    date = datetime.now()
    ticket = ""