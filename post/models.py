# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.db import models
from ckeditor.fields import RichTextField

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
	slug        = models.CharField(
				  max_length= 128,
				  blank= True,
				)
	description = models.CharField(max_length= 128)
	content     = RichTextField()
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
	def save(self, *args, **kwargs):
		slug = self.title.decode('utf-8').lower()
		regx = r'[^\w|^\d|^\s]'
		slug = re.sub(regx, '', slug).replace(' ', '-')
		self.slug, count = self.checkSlug(slug)
		super(Post, self).save(args, kwargs)

	def create(self, *args, **kwargs):
		slug = self.title.decode('utf-8').lower()
		regx = r'[^\w|^\d|^\s]'
		slug = re.sub(regx, '', slug).replace(' ', '-')
		self.slug, count = self.checkSlug(slug)
		super(Post, self).create(args, kwargs)

	def checkSlug(self, slug, count= 0):
		posts = Post.objects.filter(slug= slug)
		if ((len(posts) > 0) and (posts[0].pk != self.pk)):
			count += 1
			if (re.search(r'-[\d]$', slug)):
				slug = slug[:len(slug)-2]
			slug += '-' + str(count)
			return self.checkSlug(slug, count)
		return slug, count

	def __unicode__(self):
		return "%s" % self.title
