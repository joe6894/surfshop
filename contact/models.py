from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    full_name = models.CharField(max_length=254)
    subject = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=254)
    query_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
