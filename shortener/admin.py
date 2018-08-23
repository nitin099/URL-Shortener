from django.contrib import admin
from .models import TinyURL

# Register your models here.

class TinyURLAdmin(admin.ModelAdmin):
	list_display = ["url", "shortcode", "timestamp", "update"]

	class Meta:
		model = TinyURL

admin.site.register(TinyURL, TinyURLAdmin)