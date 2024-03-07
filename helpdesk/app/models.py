from django.db import models

# Create your models here.
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('complete', 'Complete'),
        ('inProgress', 'In Progress'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    def __str__(self):
        return self.title
    
    
class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.comment