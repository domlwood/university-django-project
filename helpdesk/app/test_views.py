import pytest
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Ticket

@pytest.mark.django_db
class TestViews:
    def test_index_get(self, client):
        # Create a user and log in
        user = User.objects.create_user(username="testuser", password="password123")
        client.login(username="testuser", password="password123")

        # Access the index view
        response = client.get(reverse('index'))
        assert response.status_code == 200, "Index view should return HTTP 200 for logged-in users."
        assert "tickets" in response.context, "Index view should include 'tickets' in context."

    def test_index_post_create_ticket(self, client):
        # Create a user and log in
        user = User.objects.create_user(username="testuser", password="password123")
        client.login(username="testuser", password="password123")

        # Submit a form to create a ticket
        response = client.post(reverse('index'), {"title": "Test Ticket"})
        assert response.status_code == 302, "Index POST should redirect after creating a ticket."
        assert Ticket.objects.filter(client=user, title="Test Ticket").exists(), "Ticket should be created."

    def test_ticket_get(self, client):
        # Create a user, ticket, and log in
        user = User.objects.create_user(username="testuser", password="password123")
        ticket = Ticket.objects.create(client=user, title="Test Ticket", description="Sample", priority="low", date=datetime.now())
        client.login(username="testuser", password="password123")

        # Access the ticket view
        response = client.get(reverse('ticket', kwargs={"id": ticket.id}))
        assert response.status_code == 200, "Ticket view should return HTTP 200."
        assert response.context["ticket"] == ticket, "Ticket view should include the ticket in context."

    def test_ticket_post_add_comment(self, client):
        # Create a user, ticket, and log in
        user = User.objects.create_user(username="testuser", password="password123")
        ticket = Ticket.objects.create(client=user, title="Test Ticket", description="Sample", priority="low", date=datetime.now())
        client.login(username="testuser", password="password123")

        # Submit a comment
        response = client.post(reverse('ticket', kwargs={"id": ticket.id}), {"comment": "Test Comment"})
        assert response.status_code == 302, "Ticket POST should redirect after adding a comment."
        assert ticket.ticketcomment_set.filter(comment="Test Comment").exists(), "Comment should be added to the ticket."

    def test_editticket_get(self, client):
        # Create a user, ticket, and log in
        user = User.objects.create_user(username="testuser", password="password123")
        ticket = Ticket.objects.create(client=user, title="Test Ticket", description="Sample", priority="low", date=datetime.now())
        client.login(username="testuser", password="password123")

        # Access the editticket view
        response = client.get(reverse('editticket', kwargs={"id": ticket.id}))
        assert response.status_code == 200, "EditTicket view should return HTTP 200."
        assert response.context["ticket"] == ticket, "EditTicket view should include the ticket in context."

    def test_editticket_post_update_ticket(self, client):
        # Create a user, ticket, and log in
        user = User.objects.create_user(username="testuser", password="password123")
        ticket = Ticket.objects.create(client=user, title="Test Ticket", description="Sample", priority="low", date=datetime.now(), status="draft")
        client.login(username="testuser", password="password123")

        # Submit a form to update the ticket
        response = client.post(reverse('editticket', kwargs={"id": ticket.id}), {
            "title": "Updated Title",
            "description": "Updated Description",
            "priority": "high"
        })
        ticket.refresh_from_db()
        assert response.status_code == 302, "EditTicket POST should redirect after updating the ticket."
        assert ticket.title == "Updated Title", "Ticket title should be updated."
        assert ticket.description == "Updated Description", "Ticket description should be updated."
        assert ticket.priority == "high", "Ticket priority should be updated."
        assert ticket.status == "inProgress", "Ticket status should change to 'inProgress'."
