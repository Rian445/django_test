from django.db import models

class RPSHistory(models.Model):
    CHOICES = (
        ('R', 'Rock'),
        ('P', 'Paper'),
        ('S', 'Scissors'),
    )
    
    RESULTS = (
        ('W', 'You win'),
        ('L', 'You lose'),
        ('T', "It's a tie"),
    )
    
    user_choice = models.CharField(max_length=1, choices=CHOICES)
    computer_choice = models.CharField(max_length=1, choices=CHOICES)
    result = models.CharField(max_length=1, choices=RESULTS)
    played_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-played_at']
    
    def __str__(self):
        return f'{self.get_user_choice_display()} vs {self.get_computer_choice_display()} → {self.get_result_display()}'
