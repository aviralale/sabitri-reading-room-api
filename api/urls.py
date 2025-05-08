from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, SubscriberViewSet, TestimonialViewSet

router = DefaultRouter()
router.register(r"contacts", ContactViewSet, basename="contact")
router.register(r"subscribers", SubscriberViewSet, basename="subscriber")
router.register(r"testimonials", TestimonialViewSet, basename="testimonial")

urlpatterns = [
    path("", include(router.urls)),
]
