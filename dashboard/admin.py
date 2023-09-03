from django.contrib import admin
from .models import Short_URL


# Register your models here.
class Short_URL_Admin(admin.ModelAdmin):
    model = Short_URL
    list_display = ("short_url", "long_url", "owner", "clicked", "created_at")


admin.site.register(Short_URL, Short_URL_Admin)
