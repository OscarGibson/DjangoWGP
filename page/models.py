# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from content.models import Content

PAGES_TYPES = (
	('blog', 'Blog'),
	('simple', 'Simple')
	)

class Page(models.Model):
	
	title      = models.CharField(
				 max_length= 32, 
				 blank= True
				 )
	subtitle   = models.CharField(
				 max_length= 32, 
				 blank= True
				 )
	slug       = models.CharField(max_length= 32)
	page_type  = models.CharField(max_length= 32, choices=PAGES_TYPES)
	background = models.ImageField(
		       upload_to="bg_images",
		       blank= True,
		       null= True
		       )
	header     = models.ForeignKey(
		       Content,
		       related_name= 'content_in_header',
		       blank= True,
		       null= True
		       )
	body       = models.ForeignKey(
		       Content,
		       related_name= 'content_in_body',
		       blank= True,
		       null= True
		       )

	def __unicode__(self):
		return "%s" % self.title