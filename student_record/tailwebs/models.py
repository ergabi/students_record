from django.db import models

class Reports(models.Model):
    student_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    mark = models.DecimalField(max_digits=5, decimal_places=2)  

    def __str__(self):
        return f"{self.student_name} - {self.subject}"