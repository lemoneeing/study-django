from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from .models import Topping, Pizza, Chef
from django.db import connection


# Create your views here.

# CBV + prefetch_related
@method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):

    def get(self, request):
        connection.queries_log.clear()

        response = HttpResponse(content_type='text/html')
        response.write(f"<h1>RESTAURANT</h1>")

        response.write(f"<p><b>Chefs Info</b></p>")

        chefs = Chef.objects.all().prefetch_related('pizza_set', 'pizza_set__toppings')
        print('\n'.join(q['sql'] for q in connection.queries_log))

        cooks = []

        chef_info_list = "<ul>"
        for chef in chefs:
            connection.queries_log.clear()
            chef_info_list += f"<li>{chef.name}({chef.rank}) - {chef.career} years of experience</li>"
            cooks.append(chef.pizza_set.all())
            print('\n'.join(q['sql'] for q in connection.queries_log))
        chef_info_list += "</ul></p>"
        response.write(chef_info_list)

        response.write(f"<p><b>Menu</b></p>")

        print('\n'.join(q['sql'] for q in connection.queries_log))
        menu_list = "<ul>"
        for cook in cooks:
            connection.queries_log.clear()
            menu_list += f"<li>{cook}</li>"
            print('\n'.join(q['sql'] for q in connection.queries_log))
        menu_list += "</ul></p>"
        response.write(menu_list)
        return response


class IndexView(ListView):
    model = Chef
    template_name = 'restaurant/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'chefs': Chef.objects.all(),
                        'menu': ['pizza'], })
        return context


# GCBV
class MenuView(ListView):
    template_name = 'restaurant/menu_cook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cook'] = self.model.__name__
        return context


class PizzaMenu(MenuView):
    model = Pizza
