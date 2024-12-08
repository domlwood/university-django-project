import pytest
from .forms import TicketInitialForm, TicketDetailForm, CommentForm

@pytest.mark.django_db
class TestForms:
    def test_ticket_initial_form_valid_data(self):
        data = {
            "title": "Test Ticket",
            "description": "This is a test description",
            "priority": "medium",
        }
        form = TicketInitialForm(data=data)
        assert form.is_valid()

    def test_ticket_initial_form_missing_title(self):
        data = {
            "description": "This is a test description",
            "priority": "medium",
        }
        form = TicketInitialForm(data=data)
        assert not form.is_valid()
        assert "title" in form.errors

    def test_ticket_detail_form_valid_data(self):
        data = {
            "title": "Detailed Ticket",
            "description": "Detailed description of the ticket",
            "priority": "high",
        }
        form = TicketDetailForm(data=data)
        assert form.is_valid()

    def test_ticket_detail_form_missing_priority(self):
        data = {
            "title": "Detailed Ticket",
            "description": "Detailed description of the ticket",
        }
        form = TicketDetailForm(data=data)
        assert not form.is_valid()
        assert "priority" in form.errors

    def test_comment_form_valid_data(self):
        data = {
            "comment": "This is a test comment",
            "ticket": "Test Ticket",
        }
        form = CommentForm(data=data)
        assert form.is_valid()

    def test_comment_form_missing_comment(self):
        data = {
            "ticket": "Test Ticket",
        }
        form = CommentForm(data=data)
        assert not form.is_valid()
        assert "comment" in form.errors
