from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MenuItems


class Main(TemplateView):
    def get(self, request, *args, **kwargs):
        menu = MenuItems.objects.filter(menu__name='test1').all()
        return render(request, 'index.html', {'object_list':menu})
