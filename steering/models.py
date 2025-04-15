from django.db import models

class SteeringPrediction(models.Model):
    speed = models.FloatField()
    predicted_angle = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Speed: {self.speed} km/h → Angle: {self.predicted_angle} radians"
