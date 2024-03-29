from django.db import models
from django.shortcuts import reverse


ROOM_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
)
BEDROOM_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
)
CATEGORY_CHOICES = (
    ("FR", "Featured"),
    ("RE", "Rent"),
)


class Agent(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, upload_to="Agents/%Y/%m/%d")
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True)
    area = models.FloatField()
    rooms = models.IntegerField(choices=ROOM_CHOICES, default=1, blank=True, null=True)
    bedroom = models.IntegerField(choices=BEDROOM_CHOICES, default=1)
    bathroom = models.IntegerField(default=1)
    garage = models.IntegerField(default=1)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50, default="MALINDI")
    listing_date = models.DateTimeField(auto_now_add=True)
    main_photo = models.ImageField(default="blackroq_3.jpg")
    photo_1 = models.ImageField(blank=True, upload_to="Property/%Y/%m/%d")
    photo_2 = models.ImageField(blank=True, upload_to="Property/%Y/%m/%d")
    photo_3 = models.ImageField(blank=True, upload_to="Property/%Y/%m/%d")
    photo_4 = models.ImageField(blank=True, upload_to="Property/%Y/%m/%d")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, default="SL")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:property_detail", kwargs={"pk": self.pk})


class Testimonial(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class VideoTestimonial(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message by {self.name}"


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, blank=False)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
