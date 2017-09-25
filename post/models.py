# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category (models.Model):
	name = models.CharField(max_length= 128)
	slug = models.CharField(max_length= 128)
	def __unicode__(self):
		return "%s" % self.name

class Tag (models.Model):
	name = models.CharField(max_length= 128)
	slug = models.CharField(max_length= 128)
	def __unicode__(self):
		return "%s" % self.name

class Post (models.Model):
	title       = models.CharField(max_length= 128)
	description = models.CharField(max_length= 128)
	content     = models.TextField()
	image       = models.ImageField(upload_to= 'posts')
	date        = models.DateTimeField(
		          auto_now_add= True,
		          auto_now= False
		          )
	category    = models.ForeignKey(
		        Category,
		        related_name= 'post_category'
		        )
	tag         = models.ManyToManyField(
		        Tag,
		        related_name= 'post_tags',
		        blank= True
		        )
	def __unicode__(self):
		return "%s" % self.title
