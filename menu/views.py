from django.shortcuts import render
from django.views.generic import View

class MenuListView(View):
    def get(self, request, *args, **kwards):
        context = {

        }
        return render(request, 'menu.html', context)