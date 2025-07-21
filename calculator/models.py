from django.db import models


class CalculationHistory(models.Model):
    """
    Model to store the history of compound interest calculations.
    """
    principle = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.IntegerField()
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    millionaire_time = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the CalculationHistory object.
        """
        return f"P: ${self.principle}, R: {self.rate}%, T: {self.time} years"

    class Meta:
        """
        Meta options for the CalculationHistory model.
        Orders records by timestamp in descending order (most recent first).
        """
        ordering = ['-timestamp']
        verbose_name_plural = "Calculation Histories"
