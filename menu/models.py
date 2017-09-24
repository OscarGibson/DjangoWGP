# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from page.models import Page

class Menu(models.Model):
	name = models.CharField(
		   max_length= 32, 
		   primary_key= True
		   )
	item = models.ManyToManyField(Page, related_name= "menu_item")
	def __unicode__(self):
		return "%s" % self.name
		
