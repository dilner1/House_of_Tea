from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    title = models.CharField(max_length=120, null=True)
    body = models.TextField(null=True, blank=False)
    urgent = models.BooleanField(default=False, null=True, blank=True)
    order_id = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.title
