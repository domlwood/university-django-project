from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Ticket
from .forms import CommentForm, TicketDetailForm, TicketInitialForm
# Create your views here.

def index(response):
    tickets = Ticket.objects.all()
    if response.method == "POST":
        form = TicketInitialForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["title"]
            d = ""
            p = "low"
            t = Ticket(title=n, description=d, priority=p, date=datetime.now())
            t.save()
            
            # Redirect to editticket view with the ID of the newly created ticket
            return redirect(reverse('editticket', args=[t.id]))
    else:
        form = TicketInitialForm()
        return render(response, "app/home.html", {"tickets": tickets, "form": form})

def ticket(response, id):
    ticket = Ticket.objects.get(id=id)
    if response.method == "POST":
        form = CommentForm(response.POST)
        if form.is_valid():
            c = form.cleaned_data["comment"]
            d = datetime.now()
            t = Ticket.objects.get(id=id)
            t.ticketcomment_set.create(comment=c, date=d)
            t.save()
            form = CommentForm()
            return render(response, "app/ticket.html", {"ticket": ticket, "form": form})
    else:
        form = CommentForm()
        return render(response, "app/ticket.html", {"ticket": ticket, "form": form})

def editticket(response, id):
    ticket = Ticket.objects.get(id=id)
    if response.method == "POST":
        if ticket.status == "draft":
            form = TicketDetailForm(response.POST)
            if form.is_valid():
                n = form.cleaned_data["title"]
                d = form.cleaned_data["description"]
                p = form.cleaned_data["priority"]
                t = Ticket.objects.get(id=id)
                t.title = n
                t.description = d
                t.priority = p
                t.status = "inProgress"
                t.save()
                form = TicketDetailForm()
                return redirect('/')

        else:
            print("Ticket is not a draft. Cannot edit.")
    else:
        form = TicketDetailForm(initial={"title": ticket.title, "description": ticket.description, "priority": ticket.priority})
        
    return render(response, "app/editticket.html", {"ticket": ticket, "form": form})
