from django.db import models
from django.contrib.auth.models import User

class ChargingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_price = models.FloatField(default=0.0)
    target_percentage = models.IntegerField(default=100)
    current_soc = models.IntegerField(default=20)
    temperature = models.FloatField(default=35.0)
    is_active = models.BooleanField(default=False)
    energy_used = models.FloatField(default=0.0) # in kWh
    start_time = models.DateTimeField(auto_now_add=True)