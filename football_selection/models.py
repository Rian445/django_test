# football_selection/models.py
from django.db import models


class SelectionHistory(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]

    STATUS_CHOICES = [
        ('SELECTED', 'Selected'),
        ('REJECTED', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    reason = models.TextField()
    decided_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-decided_at']

    def __str__(self):
        return f'{self.name} – {self.status}'
