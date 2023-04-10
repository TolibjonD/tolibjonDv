from django.db import models
from django.utils import timezone


# Create your models here.
class VisitorsInformation(models.Model):
    device = models.CharField(max_length=300)
    browser = models.CharField(max_length=300)
    os_info = models.CharField(max_length=300)
    device_pr = models.CharField(max_length=300)
    ip = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="visitors/", default="visitors/default.png")

    def __str__(self):
        return f"{ self.device_pr }: {self.ip}"

    class Meta:
        ordering = ["-created_at"]
