# -*- coding: utf-8 -*-
import urllib
from django import template
from django.utils.encoding import force_str

register = template.Library()

@register.simple_tag(takes_context = True)
def append_to_query(context, **kwargs):
    query_params = context['request'].GET.copy()
    for key, value in kwargs.items():
        query_params[key] = value
    query_string = u""
    if len(query_params):
        query_string += u"?%s" % urllib.parse.urlencode([
                (key, force_str(value)) for (key, value) in
                query_params.items() if value
                ]).replace('&', '&amp;')
    return query_string
