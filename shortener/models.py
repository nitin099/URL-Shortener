from django.db import models
from django.conf import settings
from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com
from django_hosts.resolvers import reverse
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class TinyURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs = super(TinyURLManager, self).all(*args, **kwargs).filter(active=True)
		return qs


class TinyURL(models.Model):
    url = models.CharField(max_length=500, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    #datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)
    objects = TinyURLManager()

    def __str__(self):
    	return self.url	

    def save(self, *args, **kwargs):
    	if self.shortcode is None or self.shortcode == "":
    		self.shortcode = create_shortcode(self)
    	if not "http" in self.url:
    		self.url = "http://" + self.url 
    	super(TinyURL, self).save(*args, **kwargs)

    def get_short_url(self):
    	url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
    	return url_path
