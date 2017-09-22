# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category (models.Model):
	name = models.CharField(max_length= 128)
	slug = models.CharField(max_length= 128)

class Tag (models.Model):
	name = models.CharField(max_length= 128)
	slug = models.CharField(max_length= 128)

class Post (models.Model):
	title       = models.CharField(max_length= 128)
	description = models.CharField(max_length= 128)
	content     = models.TextField()
	date        = models.DateTimeField(
		          auto_now_add= True,
		          auto_now= False
		          )
	category    = models.ForeignKey(
		        Category,
		        related_name= 'post_category'
		        )
	tag         = models.ManyToManyField(
		        Category,
		        related_name= 'post_tags'
		        )
