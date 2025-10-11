# core/decorators.py
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views import View

def auto_cache_view(view=None, *, timeout=300):
    def decorator(v):
        if isinstance(v, type) and issubclass(v, View):
            return method_decorator(cache_page(timeout), name='dispatch')(v)
        return cache_page(timeout)(v)

    if view is None:
        return decorator
    return decorator(view)