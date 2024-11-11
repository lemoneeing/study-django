from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100, blank=True, null=True)
    career = models.IntegerField()

    def __str__(self):
        return f"{self.name}({self.rank}) - {self.career} years of career"


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(to=Topping, through='Recipe', through_fields=('related_pizza', 'related_topping'))
    made_by = models.ForeignKey(Chef, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}({', '.join(t.name for t in self.toppings.all())})"


class Recipe(models.Model):
    related_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    related_topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

    class Meta:
        db_table = 'restaurant_recipe'

    def __str__(self):
        return f"Put {self.related_topping.name} in {self.related_pizza.name}"