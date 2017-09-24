from django import template
from django.template import loader
from django.utils.html import format_html

from ..models import Menu

register = template.Library()

@register.simple_tag
def top_menu(invisible=False):
	try:
		menu = Menu.objects.get(name= 'top_menu')
	except Exception as e:
		return format_html("<span>menu not found</span>")

	template = loader.get_template("menu/menu.html")
	context = {
		'items'     : menu.item.all(),
		'invisible' : invisible
	}
	return template.render(context)