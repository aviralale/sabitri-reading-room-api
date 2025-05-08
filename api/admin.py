from django.contrib import admin
from .models import Contact, Subscriber, Testimonial, Gallery


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email_address",
        "phone_number",
        "subject",
        "status",
        "created_at",
    )
    list_filter = ("status", "created_at")
    search_fields = ("name", "email_address", "phone_number", "subject", "message")


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("id", "email_address", "created_at")
    search_fields = ("email_address",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "designation", "created_at")
    search_fields = ("name", "designation")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "created_at")
    search_fields = ("title",)
