from django.db import models

# Create your models here.
from shortener.models import TinyURL


class ClickEventManager(models.Manager):
	def create_event(self, tinyInstance):
		if isinstance(tinyInstance, TinyURL):
			obj, created = self.get_or_create(tiny_url=tinyInstance)
			obj.count += 1
			obj.save()
			return obj.count
		return None


class ClickEvent(models.Model):
	tiny_url = models.OneToOneField(TinyURL)
	count = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)