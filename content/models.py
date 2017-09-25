# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

HEADING_CHOICES = (
	('h1','H1'),
	('h2','H2'),
	('h3','H3'),
	('h4','H4'),
	('h5','H5'),
	('h6','H6'),
	)

class Heading(models.Model):
	content = models.CharField(max_length= 128)
	size    = models.CharField(
			max_length= 2,
			choices= HEADING_CHOICES,
			default= HEADING_CHOICES[0]
			)
	def __unicode__(self):
		return "%s" % self.content

class Text(models.Model):
	content = models.TextField()
	def __unicode__(self):
		return "%s" % self.content
		
class Icon(models.Model):
	name        = models.CharField(max_length= 32)
	color       = models.CharField(max_length= 8)
	hover_color = models.CharField(max_length= 8)
	link        = models.URLField(
		        max_length= 64,
		        null= True,
		        blank= True
				)
	def __unicode__(self):
		return "%s" % self.name

class IconBlock(models.Model):
	icons = models.ManyToManyField(
		    Icon,
		    )
	def __unicode__(self):
		return "icons number -%s" % (self.id)

class Content(models.Model):
	heading = models.ForeignKey(
		    Heading,
		    related_name= 'heading_content',
		    blank= True,
		    null= True
		    )
	text    = models.ForeignKey(
		    Text,
		    related_name= 'text_content',
		    blank= True,
		    null= True
		    )
	icon    = models.ForeignKey(
		    IconBlock,
		    blank= True,
		    null= True
		    )
	def __unicode__(self):
		return "Content number -%s" % self.id	


