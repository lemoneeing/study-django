from django.http import HttpResponse
from django.views import View
from .models import Topping, Pizza, Chef
from django.db import connection


# Create your views here.
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
