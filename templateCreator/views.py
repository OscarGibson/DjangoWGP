# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect
import urllib2
import re, os

from distutils.dir_util import copy_tree # for collect static files to dist

from src. settings import BASE_DIR
from page.models import Page
from post.models import Post

class TemplateController():
	def __init__(
		self, 
		DOMAIN_NAME = 'http://localhost:8000',
		DIST_PATH   = 'dist',
		PAGES_PATH  = '',
		POSTS_PATH  = 'post'):

		self.pages_links = set()
		self.posts_links = set()
		self.DOMAIN_NAME = DOMAIN_NAME
		self.POSTS_URL = DOMAIN_NAME + '/' + POSTS_PATH
		self.PAGES_URL = DOMAIN_NAME
		self.DIST_PATH = os.path.join(BASE_DIR, DIST_PATH)
		self.PAGES_PATH = os.path.join(DIST_PATH, PAGES_PATH)
		self.POSTS_PATH = os.path.join(DIST_PATH, POSTS_PATH)

		self.STATIC_DIRS = ['static', 'media']

	def generate(self):
		pages = Page.objects.all()
		posts = Post.objects.all()

		self.collectObjects(pages, self.PAGES_PATH, self.PAGES_URL, self.pages_links)
		self.collectObjects(posts, self.POSTS_PATH, self.POSTS_URL, self.posts_links)

		for path in self.STATIC_DIRS:
			from_dir = os.path.join(BASE_DIR, path)
			to_dir = os.path.join(self.DIST_PATH, path)
			copy_tree(from_dir, to_dir)

		return [self.pages_links, self.posts_links]

	def collectObjects(self, objects, objects_path, objects_url, links_collection):
		for obj in objects:
			file_url = obj.slug.replace('/','')
			file_name = file_url + '.html' if file_url else 'index.html'
			file_path = os.path.join(objects_path, file_name)
			links_collection.add(file_path)
			self.parseHtml(objects_url + '/' + file_url, file_path)

	def parseHtml(self, url, path):
		html = urllib2.urlopen(url).read()
		file = open(path, 'w')
		file.write(html)
		file.close()

	def push():
		pass

@csrf_protect
def gener_push(request, *args, **kwargs):
	if request.method == 'POST':
		controller = TemplateController()
		if request.POST['action'] == 'generate':
			response = controller.generate()
		if request.POST['action'] == 'push':
			pass
		return HttpResponse(str(response))