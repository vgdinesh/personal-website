from django.db import models


class ContactForm(models.Model):
    from_email = models.EmailField(required=True)
    subject = models.CharField(required=True)
    message = models.CharField(widget=forms.Textarea, required=True)
