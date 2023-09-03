from django import forms
from .models import User_Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = User_Reviews
        fields = ["review_text", "rating"]
