from rest_framework.viewsets import ModelViewSet
from .models import Contact, Subscriber, Testimonial, Gallery
from .serializers import (
    ContactSerializer,
    SubscriberSerializer,
    TestimonialSerializer,
    GallerySerializer,
)
from .permissions import IsAdminOrCreateOnly, IsAdminOrGetOnly


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminOrCreateOnly]


class SubscriberViewSet(ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [IsAdminOrCreateOnly]


class TestimonialViewSet(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminOrGetOnly]


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAdminOrGetOnly]
