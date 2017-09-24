# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post

def post(request, post_id):
	post = get_object_or_404(Post, pk= post_id)
	template = 'post/post.html'
	context = {'post' : post}
	return render(request, template, context)