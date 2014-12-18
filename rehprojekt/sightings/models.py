from django.db import models
from django.contrib.gis.db import models as gismodels

class Country(gismodels.Model):
	"""
	Model to represent countries.
	"""

	isocode = gismodels.CharField(max_length=2)
	name = gismodels.CharField(max_length=255)
	geometry = gismodels.MultiPolygonField(srid=4326)
	objects = gismodels.GeoManager()

	def __unicode__(self):
		return '%s' % (self.name)


class Animal(models.Model):
	"""
	Model to represent animals.
	"""
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='animals.images')
	
	def __unicode__(self):
		return '%s' % (self.name)

	def image_url(self):
		return u'<img src="%s" alt="%s" width="80"></img>' %(self.image.url,self.name)
	
	image_url.allow_tags = True

class Meta:
	ordering = ['name']

class Sighting(gismodels.Model):
	"""
	Model to represent sightings.
	"""
	RATE_CHOICES = (
	(1, '*'),
	(2, '**'),
	(3, '***'),
	)

	date = gismodels.DateTimeField()
	description = gismodels.TextField()
	rate = gismodels.IntegerField(choices=RATE_CHOICES)
	animal = gismodels.ForeignKey(Animal)
	geometry = gismodels.PointField(srid=4326)
	objects = gismodels.GeoManager()
	
	def __unicode__(self):
		return '%s' % (self.date)

class Meta:
	ordering = ['date']
