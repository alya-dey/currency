from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    email_to = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



