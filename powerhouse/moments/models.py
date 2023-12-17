from django.conf import settings
from django.db import models
from django.utils import timezone


class Moment(models.Model):
    user_ids = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to="moments/", blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Moment"
        verbose_name_plural = "Moments"
