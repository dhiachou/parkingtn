# -*- coding: utf-8 -*-
from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator

User._meta.get_field('email')._unique = True

class owner(User):
	teleport=models.CharField(max_length = 20, blank=True, validators=[MinLengthValidator(8),MaxLengthValidator(8)])
	def __unicode__(self):
		return self.username

class parking(models.Model):
	namepark    = models.CharField(max_length = 128)
	proprietaire= models.ForeignKey(owner)
	nbrplace    = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(900000)]) 
	place       = models.CharField(max_length=200)     # adresse
	position    = GeopositionField()
	telephone   = models.CharField(max_length = 8, validators=[MinLengthValidator(8)])
	prix    	= models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(500000)]) 
	accept      = models.BooleanField(default=False)
	nbplacevide = models.IntegerField(default=0) 
	



