from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# for ratings
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
class RoyalHotelModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=60)
    description = models.TextField(max_length=200)
    photos = models.ImageField(upload_to="static/photos/", null=True, blank=True)
    reviews = models.ManyToManyField(User, through="User_Reviews")
    cost_per_day = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=500
    )
    average_rating = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Royal Hotel's"

    def __str__(self) -> str:
        return self.name


class User_Reviews(models.Model):
    hotel = models.ForeignKey(RoyalHotelModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MaxValueValidator(5)])

    class Meta:
        verbose_name_plural = "Reviews"
        unique_together = ("hotel", "user")


# Define a signal handler to update average_rating when a review is saved or deleted
@receiver(post_save, sender=User_Reviews)
@receiver(post_delete, sender=User_Reviews)
def update_average_rating(sender, instance, **kwargs):
    hotel = instance.hotel
    average_rating = User_Reviews.objects.filter(hotel=hotel).aggregate(Avg("rating"))[
        "rating__avg"
    ]
    hotel.average_rating = int(average_rating) or 0
    hotel.save()
