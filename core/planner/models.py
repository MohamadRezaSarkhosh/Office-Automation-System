from django.db import models

class Operator(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.last_name}"


class Device(models.Model):
    name = models.CharField(max_length=255)
    hourly_efficiency = models.PositiveIntegerField(
        help_text="Expected production per hour"
    )
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class WorkSession(models.Model):
    STATUS_CHOICES = [
        ('good' , 'خوب'),
        ('medium' , 'متوسط'),
        ('bad' , 'بد')
    ]
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_production = models.PositiveIntegerField()
    performance_status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operator} - {self.device}"
    
    