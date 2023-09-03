from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


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

    class Meta:
        verbose_name_plural = "Royal Hotel's"

    def __str__(self) -> str:
        return self.name


class User_Reviews(models.Model):
    hotel = models.ForeignKey(RoyalHotelModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=100)
    rating = models.IntegerField(validators=[MaxValueValidator(5)])

    class Meta:
        verbose_name_plural = "Reviews"
