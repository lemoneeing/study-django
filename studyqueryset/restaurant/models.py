from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(to=Topping, through='Recipe', through_fields=('related_pizza', 'related_topping'))

    def __str__(self):
        return f"{self.name}({', '.join(t.name for t in self.toppings.all())})"


class Recipe(models.Model):
    related_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    related_topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

    class Meta:
        db_table = 'restaurant_recipe'
