from django import forms
from .models import User_Reviews

RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = User_Reviews
        fields = ["review_text", "rating"]

    rating = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=RATING_CHOICES,
    )
