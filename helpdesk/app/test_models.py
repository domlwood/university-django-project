import pytest
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Ticket, TicketComment

@pytest.mark.django_db
class TestTicketModel:
    def test_create_ticket(self):
        # Create a user
        user = User.objects.create_user(username="testuser", password="password123")

        # Create a Ticket instance
        ticket = Ticket.objects.create(
            client=user,
            title="Sample Ticket",
            description="This is a test ticket.",
            priority="medium",
            date=datetime.now(),
            status="inProgress",
        )

        # Assertions
        assert ticket.client == user
        assert ticket.title == "Sample Ticket"
        assert ticket.description == "This is a test ticket."
        assert ticket.priority == "medium"
        assert ticket.status == "inProgress"
        assert str(ticket) == "Sample Ticket"

    def test_ticket_default_priority(self):
        # Create a Ticket without specifying priority
        ticket = Ticket.objects.create(
            title="Default Priority Ticket",
            description="Priority should default to low.",
            date=datetime.now(),
        )

        # Assertions
        assert ticket.priority == "low", "Default priority should be 'low'."

def test_ticket_choices():
    # Verify invalid choice raises ValidationError
    with pytest.raises(ValidationError):
        ticket = Ticket(
            title="Invalid Status Ticket",
            description="This ticket has an invalid status.",
            priority="low",
            date=datetime.now(),
            status="invalid_status",
        )
        ticket.full_clean()  # Validate the model instance explicitly


@pytest.mark.django_db
class TestTicketCommentModel:
    def test_create_comment(self):
        # Create a user and a ticket
        user = User.objects.create_user(username="testuser", password="password123")
        ticket = Ticket.objects.create(
            client=user,
            title="Comment Ticket",
            description="This ticket is for testing comments.",
            priority="high",
            date=datetime.now(),
        )

        # Create a TicketComment instance
        comment = TicketComment.objects.create(
            ticket=ticket,
            comment="This is a test comment.",
            date=datetime.now(),
            user=user,
        )

        # Assertions
        assert comment.ticket == ticket
        assert comment.comment == "This is a test comment."
        assert comment.user == user
        assert str(comment) == "This is a test comment."

    def test_comment_ticket_relationship(self):
        # Create a user, ticket, and multiple comments
        user = User.objects.create_user(username="testuser", password="password123")
        ticket = Ticket.objects.create(
            client=user,
            title="Relationship Ticket",
            description="Testing comment relationships.",
            priority="medium",
            date=datetime.now(),
        )
        comment1 = TicketComment.objects.create(
            ticket=ticket,
            comment="First comment.",
            date=datetime.now(),
            user=user,
        )
        comment2 = TicketComment.objects.create(
            ticket=ticket,
            comment="Second comment.",
            date=datetime.now(),
            user=user,
        )

        # Assertions
        assert ticket.ticketcomment_set.count() == 2
        assert ticket.ticketcomment_set.first().comment == "First comment."
