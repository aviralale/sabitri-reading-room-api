from django.db import models
from django.utils import timezone


class ContactFormStatus(models.TextChoices):
    RECEIVED = "RECEIVED", "Received"
    PENDING = "PENDING", "Pending"
    OPENED = "OPENED", "Opened"
    REVIEWED = "REVIEWED", "Reviewed"
    CLOSED = "CLOSED", "Closed"


class Contact(models.Model):
    name = models.CharField(max_length=70)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=103, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=ContactFormStatus.choices,
        default=ContactFormStatus.RECEIVED,
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Subscriber(models.Model):
    email_address = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)


class Testimonial(models.Model):
    name = models.CharField(max_length=65)
    designation = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to="testimonials/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.designation}"


class Gallery(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=40)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
