# -*- coding: utf-8 -*-
from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True

genr=(
	('payant','payant'),
	('gratuit','gratuit'),
)

class owner(User):
	teleport=models.CharField(max_length = 20, blank=True)
	def __unicode__(self):
		return self.username

class parking(models.Model):
	namepark    =models.CharField(max_length = 128)
	proprietaire=models.ForeignKey(owner)
	nbrplace    =models.IntegerField(default=0) 
	place       =models.CharField(max_length=200)     # adresse
	position    =GeopositionField()
	telephone   = models.CharField(max_length = 15)
	genre = models.CharField(max_length=30, choices=genr)
	accept      = models.BooleanField(default=False)
	nbplacevide  =models.IntegerField(default=0) 
	



