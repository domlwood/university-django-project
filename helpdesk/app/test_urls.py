import pytest
from django.urls import reverse, resolve
from .views import index, ticket, editticket


@pytest.mark.urls("helpdesk.urls")
class TestURLs:
    def test_index_url(self):
        # Test the '/' URL
        path = reverse("index")
        assert path == "/", "The reverse URL for 'index' should be '/'."
        resolved = resolve(path)
        assert (
            resolved.func == index
        ), "The 'index' URL should resolve to the correct view."

    def test_ticket_url(self):
        # Test the '/ticket/<int:id>' URL
        path = reverse("ticket", kwargs={"id": 1})
        assert (
            path == "/ticket/1"
        ), "The reverse URL for 'ticket' with id=1 should be '/ticket/1'."
        resolved = resolve(path)
        assert (
            resolved.func == ticket
        ), "The 'ticket' URL should resolve to the correct view."

    def test_edit_ticket_url(self):
        # Test the '/edit-ticket/<int:id>' URL
        path = reverse("editticket", kwargs={"id": 2})
        assert (
            path == "/edit-ticket/2"
        ), "The reverse URL for 'editticket' with id=2 should be '/edit-ticket/2'."
        resolved = resolve(path)
        assert (
            resolved.func == editticket
        ), "The 'editticket' URL should resolve to the correct view."
